"""
test_time_to_threshold.py — drugi cel Omega: czas do przekroczenia progu
D, na zwalidowanym rdzeniu B (lokalne eq + spojny defect). Baseline =
D(t) (Omega0, ustalone w poprzednim kroku). Testujemy, czy cokolwiek bije
baseline na TYM konkretnym zadaniu (nie na hotspot top-10 z poprzedniego
testu - to inne zadanie, inna metryka).

Kandydaci:
  - D(t)                         -> oczekiwany kierunek: WIEKSZE D(t) = KROTSZY czas do progu (rho ujemne)
  - D(t) + |R(t)|  (Omega1)      -> kontrola spojnosci z poprzednim wynikiem
  - ekstrapolacja liniowa:
      predicted_time = (thr - D(t)) / max(v(t), eps), v(t)=D(t)-D(t-1)
    -> oczekiwany kierunek: WIEKSZY predicted_time = DLUZSZY realny czas (rho dodatnie)
"""
import numpy as np
from scipy.stats import spearmanr
from timdr_quantum_lattice_variants import TIMDRQuantumLatticeVariant

SIZE = 10
N_SEEDS = 15
BURN_IN = 10   # przy 50 system juz prawie nie generuje nowych przekroczen (za wolna dynamika)
MAX_HORIZON = 40
PCTL = 25
DIRECTION = "below"   # "below" = zdarzenie to USTABILIZOWANIE (D spada ponizej progu) - to
                       # ma wiecej sensu fizycznego na tym rdzeniu (monotoniczne osiadanie w eq)
PARAMS = dict(helix_mode="local_eq", helix_coef=0.05, temp=0.01, noise=0.001)


def grid(model, fn):
    return np.array([[fn(x, y) for y in range(SIZE)] for x in range(SIZE)])


rho_D, rho_omega1, rho_extrap = [], [], []
prec_D, prec_omega1, prec_extrap = [], [], []
n_crossed_list = []

VELOCITY_WINDOW = 5  # 1-krokowa roznica jest zdominowana przez szum (noise=0.001 >> typowy
                      # dryf/krok) - usredniona predkosc z kilku krokow filtruje ten szum

for seed in range(N_SEEDS):
    model = TIMDRQuantumLatticeVariant(size=SIZE, seed=seed, **PARAMS)
    for _ in range(BURN_IN - VELOCITY_WINDOW):
        model.meta_evolution()
    D_hist = [grid(model, model.defect_operator)]
    for _ in range(VELOCITY_WINDOW):
        model.meta_evolution()
        D_hist.append(grid(model, model.defect_operator))
    D_t = D_hist[-1]                                       # D(t)
    R_t = grid(model, lambda x, y: abs(model.resonance_operator(x, y)))
    v_t = (D_hist[-1] - D_hist[0]) / VELOCITY_WINDOW        # usredniona predkosc na 5 krokach

    thr = np.percentile(D_t, PCTL)

    cmp = (lambda a: a < thr) if DIRECTION == "below" else (lambda a: a > thr)
    already_above = cmp(D_t.flatten())
    first_cross = np.full(SIZE * SIZE, MAX_HORIZON + 1)
    crossed = already_above.copy()  # nie liczymy jako "przekroczenie" tego co juz spelnia warunek
    first_cross[already_above] = 0

    for h in range(1, MAX_HORIZON + 1):
        model.meta_evolution()
        D_h = grid(model, model.defect_operator).flatten()
        newly = (~crossed) & cmp(D_h)
        first_cross[newly] = h
        crossed = crossed | newly

    mask = crossed & (~already_above)  # tylko realne, niecenzurowane przekroczenia
    n_crossed_list.append(mask.sum())
    if mask.sum() < 10:
        continue

    # naprawa bledu znaku: dla direction="below" komorka zblia sie do progu gdy
    # v_t<0 (D maleje). np.maximum(v_t,eps) bledne floorowalo ujemne predkosci
    # do +eps, dajac fikcyjnie ujemny/zerowy czas dla WIEKSZOSCI komorek. Poprawnie:
    # dystans do progu / (tempo zblizania, dodatnie gdy realnie sie zbliza).
    eps = 1e-6
    if DIRECTION == "below":
        distance = D_t.flatten() - thr           # >0 dla komorek jeszcze nad progiem
        closing_rate = np.maximum(-v_t.flatten(), eps)  # dodatnie gdy D maleje (zbliza sie)
    else:
        distance = thr - D_t.flatten()
        closing_rate = np.maximum(v_t.flatten(), eps)
    predicted_time = np.clip(distance / closing_rate, 0, MAX_HORIZON * 3)

    actual = first_cross[mask]
    rD, _ = spearmanr(D_t.flatten()[mask], actual)
    rO1, _ = spearmanr((D_t + R_t).flatten()[mask], actual)
    rEx, _ = spearmanr(predicted_time[mask], actual)
    rho_D.append(rD); rho_omega1.append(rO1); rho_extrap.append(rEx)

    k = min(10, mask.sum())
    idx_masked = np.where(mask)[0]
    order_actual = idx_masked[np.argsort(actual)[:k]]          # k komorek ktore przekrocza NAJSZYBCIEJ
    top_actual = set(order_actual.tolist())

    def topk_soonest(score_masked, higher_means_sooner):
        s = score_masked if higher_means_sooner else -score_masked
        order = idx_masked[np.argsort(-s)[:k]]
        return set(order.tolist())

    # direction="below": zdarzenie to D spadajace PONIZEJ progu (stabilizacja) ->
    # NIZSZE D(t) = BLIZEJ progu = SZYBCIEJ. Dla direction="above" byloby odwrotnie.
    level_higher_means_sooner = (DIRECTION == "above")
    top_D = topk_soonest(D_t.flatten()[mask], higher_means_sooner=level_higher_means_sooner)
    top_O1 = topk_soonest((D_t + R_t).flatten()[mask], higher_means_sooner=level_higher_means_sooner)
    top_Ex = topk_soonest(predicted_time[mask], higher_means_sooner=False)  # mniejszy predicted_time = szybciej

    prec_D.append(len(top_D & top_actual) / k)
    prec_omega1.append(len(top_O1 & top_actual) / k)
    prec_extrap.append(len(top_Ex & top_actual) / k)

print(f"N_SEEDS z wystarczajaca liczba przekroczen: {len(rho_D)}/{N_SEEDS} "
      f"(srednio {np.mean(n_crossed_list):.0f}/100 komorek 'ustabilizowalo sie' [D spadlo ponizej p{PCTL}] w oknie {MAX_HORIZON}, burn_in={BURN_IN})")
print(f"zdarzenie = D(t) spada PONIZEJ p{PCTL} (komorka osiada blisko wlasnego eq)\n")

def report(name, rho_list, prec_list, expect):
    print(f"{name}")
    print(f"  Spearman vs realny czas-do-progu: srednia={np.nanmean(rho_list):.3f} "
          f"std={np.nanstd(rho_list):.3f}  [{np.nanmin(rho_list):.3f}, {np.nanmax(rho_list):.3f}]  "
          f"(oczekiwany kierunek: {expect})")
    print(f"  top-k trafien 'kto ustabilizuje sie najszybciej': {np.mean(prec_list)*10:.1f}/10  (baza losowa: 1.0/10)\n")

level_expect = "ujemny" if DIRECTION == "above" else "dodatni"
report("D(t) [BASELINE, Omega0]", rho_D, prec_D, level_expect)
report("D(t)+|R(t)| [Omega1]", rho_omega1, prec_omega1, level_expect)
report("ekstrapolacja liniowa (thr-D)/v", rho_extrap, prec_extrap, "dodatni")

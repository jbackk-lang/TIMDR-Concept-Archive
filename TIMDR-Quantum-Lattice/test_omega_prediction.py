"""
test_omega_prediction.py — czy Ω (omega_stability_map) rzeczywiscie
"przewiduje przyszle hotspoty dekoherencji", czy tylko opisuje STAN OBECNY?

Metoda (ten sam rygor co poprzednie testy w tej rozmowie): checkpoint w
czasie t, zapisz Omega_t (siatka 10x10 -> 100 wartosci), kontynuuj
symulacje o K krokow, policz REALNA "przyszla niestabilnosc" per komorka
(srednia defect_operator w oknie t+1..t+K, ORAZ osobno wariancja fazy w
tym oknie jako niezalezna miara "ile sie realnie zmienilo"), i skoreluj
Omega_t z ta realna przyszloscia. Powtorzone dla wielu ziaren losowych,
zeby odroznic prawdziwy efekt od szumu.
"""
import math
import numpy as np
from timdr_quantum_lattice_original import TIMDRQuantumLattice

BURN_IN = 50
K_FUTURE = 20
SIZE = 10
N_SEEDS = 15


def realized_future_instability(model, k_future):
    """Kontynuuje symulacje o k_future krokow, zwraca per-komorke:
    (a) srednia defect_operator w oknie, (b) wariancje fazy w oknie -
    dwie niezalezne miary 'ile sie realnie stalo'."""
    size = model.size
    defect_hist = [[[] for _ in range(size)] for _ in range(size)]
    phase_hist = [[[] for _ in range(size)] for _ in range(size)]
    for _ in range(k_future):
        model.meta_evolution()
        for x in range(size):
            for y in range(size):
                defect_hist[x][y].append(model.defect_operator(x, y))
                phase_hist[x][y].append(model.lattice[x][y])
    mean_defect = np.array([[np.mean(defect_hist[x][y]) for y in range(size)] for x in range(size)])
    # wariancja fazy - uwaga na periodycznosc (2pi), liczymy przez sin/cos
    phase_var = np.zeros((size, size))
    for x in range(size):
        for y in range(size):
            ph = np.array(phase_hist[x][y])
            c, s = np.mean(np.cos(ph)), np.mean(np.sin(ph))
            R = math.hypot(c, s)  # mean resultant length; 1=brak zmiennosci, 0=duza
            phase_var[x][y] = 1 - R
    return mean_defect, phase_var


def corr(a, b):
    a, b = a.flatten(), b.flatten()
    if np.std(a) < 1e-12 or np.std(b) < 1e-12:
        return float('nan')
    return float(np.corrcoef(a, b)[0, 1])


results_defect = []
results_phasevar = []
results_baseline_defect_now = []  # kontrola: sam obecny defekt (bez resonance) vs przyszlosc

for seed in range(N_SEEDS):
    model = TIMDRQuantumLattice(size=SIZE, temp=0.01, noise=0.001, seed=seed)
    for _ in range(BURN_IN):
        model.meta_evolution()

    omega_t = np.array(model.omega_stability_map())
    defect_now = np.array([[model.defect_operator(x, y) for y in range(SIZE)] for x in range(SIZE)])

    mean_defect_future, phase_var_future = realized_future_instability(model, K_FUTURE)

    r_omega_defect = corr(omega_t, mean_defect_future)
    r_omega_phasevar = corr(omega_t, phase_var_future)
    r_baseline = corr(defect_now, mean_defect_future)

    results_defect.append(r_omega_defect)
    results_phasevar.append(r_omega_phasevar)
    results_baseline_defect_now.append(r_baseline)

print(f"N_SEEDS={N_SEEDS}, BURN_IN={BURN_IN}, K_FUTURE={K_FUTURE}, SIZE={SIZE}x{SIZE} (100 komorek/seed)")
print("\nKorelacja Omega_t (rzekoma 'predykcja') vs realna przyszla niestabilnosc:")
print(f"  vs mean(defect) w oknie t+1..t+{K_FUTURE}:  "
      f"srednia r={np.nanmean(results_defect):.3f}  std={np.nanstd(results_defect):.3f}  "
      f"[min={np.nanmin(results_defect):.3f}, max={np.nanmax(results_defect):.3f}]")
print(f"  vs zmiennosc fazy (1-R) w tym samym oknie: "
      f"srednia r={np.nanmean(results_phasevar):.3f}  std={np.nanstd(results_phasevar):.3f}  "
      f"[min={np.nanmin(results_phasevar):.3f}, max={np.nanmax(results_phasevar):.3f}]")
print(f"\nKontrola: sam obecny defect_operator (BEZ resonance, bez calego Omega) vs to samo:")
print(f"  r={np.nanmean(results_baseline_defect_now):.3f}  std={np.nanstd(results_baseline_defect_now):.3f}")

print(f"\nIle z {N_SEEDS} ziaren dalo r > 0.3 (Omega vs mean_defect_future)? "
      f"{sum(1 for r in results_defect if r > 0.3)}")
print(f"Ile dalo r < 0 (odwrotny kierunek)? {sum(1 for r in results_defect if r < 0)}")

"""
sweep_variants.py — ten sam pipeline testowy (rozrzut fazy + trwalosc
top-10 D(t)) co sweep_dynamics.py, teraz na wariantach A (rotator) i B
(lokalne rownowagi) helix_operator zaproponowanych przez uzytkownika.
"""
import math
import numpy as np
from timdr_quantum_lattice_variants import TIMDRQuantumLatticeVariant

SIZE = 10
N_SEEDS = 8
BURN_INS = [0, 10, 50, 200]
PERSISTENCE_GAPS = [5, 10, 15]

CONFIGS = {
    "ORYGINAL (kontrola, helix=sin(phase)*0.05)": dict(helix_mode="original", helix_coef=0.05, temp=0.01, noise=0.001),
    "A: rotator (bez self-attractora)":            dict(helix_mode="rotator",  helix_coef=0.05, temp=0.01, noise=0.001),
    "B: lokalne rownowagi (heterogeniczne)":        dict(helix_mode="local_eq", helix_coef=0.05, temp=0.01, noise=0.001),
}


def circular_dispersion(phases_flat):
    c, s = np.mean(np.cos(phases_flat)), np.mean(np.sin(phases_flat))
    return 1 - math.hypot(c, s)


def top10(mat):
    flat = np.array(mat).flatten()
    return set(np.argsort(flat)[-10:].tolist())


def eq_proximity(model):
    """Tylko dla wariantu B: jak blisko kazda komorka jest wlasnego eq -
    srednia |roznica katowa| (0 = idealnie na miejscu, pi = jak najdalej)."""
    import numpy as np
    diffs = []
    for x in range(model.size):
        for y in range(model.size):
            d = abs(model.lattice[x][y] - model.equilibrium[x][y])
            d = min(d, 2*math.pi - d)
            diffs.append(d)
    return float(np.mean(diffs))


def run_config(name, params):
    print(f"\n{'='*76}\n{name}  {params}\n{'='*76}")
    for burn_in in BURN_INS:
        dispersions = []
        persistence = {g: [] for g in PERSISTENCE_GAPS}
        eq_prox = []
        for seed in range(N_SEEDS):
            model = TIMDRQuantumLatticeVariant(size=SIZE, seed=seed, **params)
            for _ in range(burn_in):
                model.meta_evolution()

            phases = np.array(model.lattice).flatten()
            dispersions.append(circular_dispersion(phases))
            if params["helix_mode"] == "local_eq":
                eq_prox.append(eq_proximity(model))

            checkpoints = {0: top10([[model.defect_operator(x, y) for y in range(SIZE)] for x in range(SIZE)])}
            max_gap = max(PERSISTENCE_GAPS)
            for step in range(1, max_gap + 1):
                model.meta_evolution()
                if step in PERSISTENCE_GAPS:
                    checkpoints[step] = top10([[model.defect_operator(x, y) for y in range(SIZE)] for x in range(SIZE)])
            for g in PERSISTENCE_GAPS:
                persistence[g].append(len(checkpoints[0] & checkpoints[g]) / 10)

        disp_mean = np.mean(dispersions)
        line = f"  burn_in={burn_in:3d}  rozrzut fazy: {disp_mean:.3f}"
        if eq_prox:
            line += f"  | odleglosc od wlasnego eq: {np.mean(eq_prox):.3f} rad (pi={math.pi:.2f}=max, losowo~{math.pi/2:.2f})"
        print(line)
        pers_str = "  ".join(f"t+{g}:{np.mean(persistence[g])*10:.1f}/10" for g in PERSISTENCE_GAPS)
        print(f"           trwalosc top-10 D(t): {pers_str}")


for name, params in CONFIGS.items():
    run_config(name, params)

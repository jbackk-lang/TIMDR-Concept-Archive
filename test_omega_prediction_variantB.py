"""
test_omega_prediction_variantB.py — ten sam test co pierwszy raz
(test_omega_prediction.py), teraz na zwalidowanym rdzeniu wariantu B
(lokalne rownowagi + spojny defect_operator), zamiast na oryginale ktory
kolapsowal do jednego punktu.

Pytanie: czy Omega(t) = defect + |resonance| trafia w prawdziwe hotspoty
D(t+1), na krajobrazie ktory tym razem faktycznie ma co przewidywac?
"""
import math
import numpy as np
from scipy.stats import spearmanr
from timdr_quantum_lattice_variants import TIMDRQuantumLatticeVariant

SIZE = 10
N_SEEDS = 15
PARAMS = dict(helix_mode="local_eq", helix_coef=0.05, temp=0.01, noise=0.001)


def top_k_idx(mat, k=10):
    return set(int(i) for i in np.argsort(np.array(mat).flatten())[-k:])


def run(burn_in):
    rho_omega_list, rho_D_list = [], []
    prec_omega_list, prec_D_list = [], []
    for seed in range(N_SEEDS):
        model = TIMDRQuantumLatticeVariant(size=SIZE, seed=seed, **PARAMS)
        for _ in range(burn_in):
            model.meta_evolution()

        D_t = np.array([[model.defect_operator(x, y) for y in range(SIZE)] for x in range(SIZE)])
        Omega_t = np.array(model.omega_stability_map())

        model.meta_evolution()
        D_t1 = np.array([[model.defect_operator(x, y) for y in range(SIZE)] for x in range(SIZE)])

        rho_omega, _ = spearmanr(Omega_t.flatten(), D_t1.flatten())
        rho_D, _ = spearmanr(D_t.flatten(), D_t1.flatten())
        rho_omega_list.append(rho_omega)
        rho_D_list.append(rho_D)

        top_actual = top_k_idx(D_t1)
        prec_omega_list.append(len(top_k_idx(Omega_t) & top_actual) / 10)
        prec_D_list.append(len(top_k_idx(D_t) & top_actual) / 10)

    print(f"\nburn_in={burn_in}  (N_SEEDS={N_SEEDS})")
    print(f"  Spearman Omega(t) vs D(t+1): srednia={np.nanmean(rho_omega_list):.3f} "
          f"std={np.nanstd(rho_omega_list):.3f}  [{np.nanmin(rho_omega_list):.3f}, {np.nanmax(rho_omega_list):.3f}]")
    print(f"  Spearman D(t)     vs D(t+1): srednia={np.nanmean(rho_D_list):.3f} "
          f"std={np.nanstd(rho_D_list):.3f}  [{np.nanmin(rho_D_list):.3f}, {np.nanmax(rho_D_list):.3f}]")
    print(f"  Top-10 trafien Omega->D(t+1): {np.mean(prec_omega_list)*10:.1f}/10  "
          f"({sum(1 for r in rho_omega_list if r>0.3)}/{N_SEEDS} ziaren z rho>0.3, "
          f"{sum(1 for r in rho_omega_list if r<0)}/{N_SEEDS} ujemnych)")
    print(f"  Top-10 trafien D(t)->D(t+1):   {np.mean(prec_D_list)*10:.1f}/10  (baza losowa: 1.0/10)")


for bi in [50, 200]:
    run(bi)

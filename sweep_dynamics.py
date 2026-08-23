"""
sweep_dynamics.py — plan strojenia uzytkownika: sprawdz, przy jakich
parametrach siatka NIE kolapsuje do jednego punktu stalego (~pi), i czy
top-10 D(t) to trwale plamy w czasie, czy szum przemalowujacy sie co krok.
Kryteria sukcesu dokladnie jak zaproponowano - bez Omega.
"""
import math
import numpy as np
from timdr_quantum_lattice_tunable import TIMDRQuantumLattice

SIZE = 10
N_SEEDS = 8
BURN_INS = [0, 10, 50]
PERSISTENCE_GAPS = [5, 10, 15]  # sprawdz top-10 D(t) vs D(t+gap)

PROFILES = {
    "A: blisko punktu stalego (oryginal)": dict(helix_coef=0.05, temp=0.01, noise=0.001),
    "B: pol-stabilny":                      dict(helix_coef=0.01, temp=0.05, noise=0.01),
    "C: chaos":                             dict(helix_coef=0.005, temp=0.10, noise=0.01),
}


def circular_dispersion(phases_flat):
    """1 - R, R = dlugosc sredniego wektora wypadkowego. 0 = wszystko w
    jednym punkcie, ~1 = rozrzucone po calym kole."""
    c, s = np.mean(np.cos(phases_flat)), np.mean(np.sin(phases_flat))
    return 1 - math.hypot(c, s)


def top10(mat):
    flat = np.array(mat).flatten()
    return set(np.argsort(flat)[-10:].tolist())


def run_profile(name, params):
    print(f"\n{'='*72}\n{name}  {params}\n{'='*72}")
    for burn_in in BURN_INS:
        dispersions = []
        persistence = {g: [] for g in PERSISTENCE_GAPS}
        for seed in range(N_SEEDS):
            model = TIMDRQuantumLattice(size=SIZE, seed=seed, **params)
            for _ in range(burn_in):
                model.meta_evolution()

            phases = np.array(model.lattice).flatten()
            dispersions.append(circular_dispersion(phases))

            checkpoints = {}
            checkpoints[0] = top10([[model.defect_operator(x, y) for y in range(SIZE)] for x in range(SIZE)])
            max_gap = max(PERSISTENCE_GAPS)
            for step in range(1, max_gap + 1):
                model.meta_evolution()
                if step in PERSISTENCE_GAPS:
                    checkpoints[step] = top10([[model.defect_operator(x, y) for y in range(SIZE)] for x in range(SIZE)])
            for g in PERSISTENCE_GAPS:
                overlap = len(checkpoints[0] & checkpoints[g]) / 10
                persistence[g].append(overlap)

        disp_mean, disp_std = np.mean(dispersions), np.std(dispersions)
        print(f"  burn_in={burn_in:3d}  rozrzut fazy (1-R): srednia={disp_mean:.3f} std={disp_std:.3f}  "
              f"(0=kolaps do 1 punktu, ~1=rozrzucone)")
        for g in PERSISTENCE_GAPS:
            p = persistence[g]
            print(f"           top-10 D(t) vs D(t+{g:2d}): trwalosc={np.mean(p)*10:.1f}/10  "
                  f"(losowa baza ~{10*10/100:.1f}/10 gdyby kazdy krok losowal od nowa)")


for name, params in PROFILES.items():
    run_profile(name, params)

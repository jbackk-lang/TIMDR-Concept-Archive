"""
timdr_quantum_lattice_variants.py — dwa warianty helix_operator
zaproponowane przez uzytkownika, wstrzykniete w ten sam szkielet, zeby dalo
sie je przepuscic przez ten sam pipeline testowy (dispersion + trwalosc
top-10) co wczesniej.
"""
import math
import random


class TIMDRQuantumLatticeVariant:
    def __init__(self, size, temp=0.01, noise=0.001, helix_mode="original",
                 helix_coef=0.05, seed=None):
        self.size = size
        self.temp = temp
        self.noise = noise
        self.helix_mode = helix_mode  # "original" | "rotator" | "local_eq"
        self.helix_coef = helix_coef
        rng = random.Random(seed)
        self.lattice = [[rng.uniform(0, 2*math.pi) for _ in range(size)] for _ in range(size)]
        # wariant B: lokalne rownowagi, wlasne "ulubione" phi* na komorke
        self.equilibrium = [[rng.uniform(0, 2*math.pi) for _ in range(size)] for _ in range(size)]
        self._rng = rng

    def helix_operator(self, x, y):
        phase = self.lattice[x][y]
        if self.helix_mode == "original":
            twist = math.sin(phase) * self.helix_coef
            return phase + twist
        elif self.helix_mode == "rotator":
            twist = self.helix_coef + self._rng.uniform(-0.01, 0.01)
            return (phase + twist) % (2 * math.pi)
        elif self.helix_mode == "local_eq":
            eq = self.equilibrium[x][y]
            twist = math.sin(eq - phase) * self.helix_coef
            return (phase + twist) % (2 * math.pi)
        else:
            raise ValueError(self.helix_mode)

    def defect_operator(self, x, y):
        phase = self.lattice[x][y]
        if self.helix_mode == "local_eq":
            # naprawa niespojnosci: defekt mierzy realna odleglosc katowa od
            # WLASNEGO eq[x][y] (0 w eq, max=temp antypodalnie), nie od
            # globalnego 0/pi jak w oryginale. |cos(phase-eq)| odtworzylby
            # ten sam blad (dwa maksima - w eq i w eq+pi), wiec uzywam
            # monotonicznej wersji: (1-cos(delta))/2, delta = phase-eq.
            eq = self.equilibrium[x][y]
            return (1 - math.cos(phase - eq)) / 2 * self.temp
        return abs(math.cos(phase)) * self.temp

    def resonance_operator(self, x, y):
        phase = self.lattice[x][y]
        neighbors = []
        if x > 0: neighbors.append(self.lattice[x-1][y])
        if x < self.size-1: neighbors.append(self.lattice[x+1][y])
        if y > 0: neighbors.append(self.lattice[x][y-1])
        if y < self.size-1: neighbors.append(self.lattice[x][y+1])
        if not neighbors:
            return 0
        avg = sum(neighbors) / len(neighbors)
        return math.sin(avg - phase) * 0.1

    def meta_evolution(self):
        new_lattice = []
        for x in range(self.size):
            row = []
            for y in range(self.size):
                h = self.helix_operator(x, y)
                d = self.defect_operator(x, y)
                r = self.resonance_operator(x, y)
                new_phase = h + r - d + self._rng.uniform(-self.noise, self.noise)
                row.append(new_phase % (2 * math.pi))
            new_lattice.append(row)
        self.lattice = new_lattice

    def omega_stability_map(self):
        return [[self.defect_operator(x, y) + abs(self.resonance_operator(x, y))
                  for y in range(self.size)] for x in range(self.size)]

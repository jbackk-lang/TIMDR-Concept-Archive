"""
timdr_quantum_lattice_tunable.py — ten sam model co timdr_quantum_lattice.py,
z dwiema jedynymi zmianami: helix_coef i mozliwoscia podania wlasnego
temp/noise (juz byly parametrami __init__, tylko helix mial 0.05 na sztywno
w kodzie). Zadnych nowych operatorow - dokladnie plan strojenia uzytkownika.
"""
import math
import random


class TIMDRQuantumLattice:
    def __init__(self, size, temp=0.01, noise=0.001, helix_coef=0.05, seed=None):
        self.size = size
        self.temp = temp
        self.noise = noise
        self.helix_coef = helix_coef
        rng = random.Random(seed)
        self.lattice = [[rng.uniform(0, 2*math.pi) for _ in range(size)] for _ in range(size)]
        self._rng = rng

    def helix_operator(self, x, y):
        phase = self.lattice[x][y]
        twist = math.sin(phase) * self.helix_coef
        return phase + twist

    def defect_operator(self, x, y):
        phase = self.lattice[x][y]
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

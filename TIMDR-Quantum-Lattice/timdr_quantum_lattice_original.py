"""
timdr_quantum_lattice_original.py — dokladny, niezmieniony punkt wyjscia
(kod uzytkownika sprzed diagnozy). Zachowany dla historii/reprodukcji.

Zastrzezenie: to jest klasyczny model sprzezonych oscylatorow fazowych
(rodzina Kuramoto), nie mechanika kwantowa - brak wektora stanu, zespolonej
amplitudy, unitarnej ewolucji, pomiaru czy splatania. Nazwy "kubit" /
"dekoherencja" / "interferencja" sa kosmetyczne, nie odpowiadaja formalizmowi
kwantowemu. Patrz README.md w tym repo po pelna diagnoze i zwalidowany
nastepca (timdr_quantum_lattice_variants.py, tryb "local_eq").

Znany problem tej wersji: helix_operator ma globalny punkt staly w fazie=pi
(pochodna mapy 1-c, stabilna dla 0<c<2) - siatka kolapsuje do jednego,
prawie jednorodnego stanu w ~50 krokach niezaleznie od ziarna losowego, wiec
omega_stability_map() nie ma tu bogatego krajobrazu do przewidywania.
"""
import math
import random
class TIMDRQuantumLattice:
    def __init__(self, size, temp=0.01, noise=0.001, seed=None):
        self.size = size
        self.temp = temp
        self.noise = noise
        rng = random.Random(seed)
        self.lattice = [
            [rng.uniform(0, 2*math.pi) for _ in range(size)]
            for _ in range(size)
        ]
        self._rng = rng

    def helix_operator(self, x, y):
        phase = self.lattice[x][y]
        twist = math.sin(phase) * 0.05
        return phase + twist

    def defect_operator(self, x, y):
        phase = self.lattice[x][y]
        instability = abs(math.cos(phase)) * self.temp
        return instability

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
        resonance = math.sin(avg - phase) * 0.1
        return resonance

    def meta_evolution(self):
        new_lattice = []
        for x in range(self.size):
            row = []
            for y in range(self.size):
                h = self.helix_operator(x, y)
                d = self.defect_operator(x, y)
                r = self.resonance_operator(x, y)
                new_phase = h + r - d + self._rng.uniform(-self.noise, self.noise)
                new_phase = new_phase % (2 * math.pi)
                row.append(new_phase)
            new_lattice.append(row)
        self.lattice = new_lattice

    def omega_stability_map(self):
        stability_map = []
        for x in range(self.size):
            row = []
            for y in range(self.size):
                d = self.defect_operator(x, y)
                r = abs(self.resonance_operator(x, y))
                score = d + r
                row.append(score)
            stability_map.append(row)
        return stability_map

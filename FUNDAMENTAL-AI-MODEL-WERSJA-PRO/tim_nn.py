
import numpy as np

class TIM_NN:
    def __init__(self, N=100, tau=0.01, rho_krit=0.2):
        self.N = N
        self.tau = tau
        self.rho_krit = rho_krit
        self.x = np.zeros(N)

    def step(self):
        x_new = np.zeros_like(self.x)

        # propagacja (Λ + TIDER)
        for i in range(self.N):
            x_new[i] = np.tanh(self.x[i-1])

        # skręt (τ)
        x_new[0] += self.tau

        # gradient (ρ)
        rho = np.abs(np.diff(np.concatenate([x_new, x_new[:1]])))

        # próg aktualizacji (J)
        if np.max(rho) > self.rho_krit:
            x_new = np.tanh(2 * x_new)

        self.x = x_new

    def run(self, steps=1000):
        for _ in range(steps):
            self.step()
        return self.x

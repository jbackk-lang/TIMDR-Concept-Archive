
import numpy as np

class TIMTopoGeneratorDoubleMem:
    def __init__(self, N=100, K1=32, K2=16, tau1=0.02, tau2=0.01):
        """
        N  - liczba węzłów (pętla Λ)
        K1 - rozmiar pierwszej pamięci (h1)
        K2 - rozmiar drugiej pamięci (h2)
        """
        self.N = N
        self.K1 = K1
        self.K2 = K2
        self.tau1 = tau1
        self.tau2 = tau2

        # pamięci
        self.h1 = np.zeros(K1)
        self.h2 = np.zeros(K2)

        # wagi topologiczne
        self.W_h1 = 0.1 * np.random.randn(K1, N)   # Λ -> h1
        self.W_h2 = 0.1 * np.random.randn(K2, K1)  # h1 -> h2
        self.W_out = 0.1 * np.random.randn(N, K2)  # h2 -> x_gen

    def step(self, x_prev=None):
        """
        Jeden krok generacji topologicznej.
        x_prev - poprzedni stan pętli (N) lub None (start losowy)
        """

        if x_prev is None:
            x_prev = 0.1 * np.random.randn(self.N)

        # Λ: pętla – mieszamy sąsiadów (topologia)
        x_loop = 0.5 * x_prev + 0.25 * np.roll(x_prev, 1) + 0.25 * np.roll(x_prev, -1)

        # pierwsza pamięć h1 (z τ1)
        h1_in = self.W_h1 @ x_loop
        h1_new = np.tanh(h1_in + self.tau1)

        # druga pamięć h2 (z τ2)
        h2_in = self.W_h2 @ h1_new
        h2_new = np.tanh(h2_in + self.tau2)

        # rekurencja pamięci (podwójna pamięć)
        self.h1 = 0.5 * self.h1 + 0.5 * h1_new
        self.h2 = 0.5 * self.h2 + 0.5 * h2_new

        # generacja nowego stanu z h2
        x_gen = np.tanh(self.W_out @ self.h2)

        return x_gen

    def generate_sequence(self, steps=100):
        """
        Generuje sekwencję stanów topologicznych.
        """
        seq = []
        x = None
        for _ in range(steps):
            x = self.step(x_prev=x)
            seq.append(x.copy())
        return np.array(seq)

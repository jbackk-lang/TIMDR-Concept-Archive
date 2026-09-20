
import numpy as np

class TIMAutoencoder:
    def __init__(self, N=100, K=16, tau=0.01, rho_krit=0.2):
        """
        N - liczba węzłów wejścia/wyjścia (pętla)
        K - rozmiar kodu (pamięć / warstwa ukryta)
        """
        self.N = N
        self.K = K
        self.tau = tau
        self.rho_krit = rho_krit

        # stany
        self.x = np.zeros(N)   # wejście / rekonstrukcja
        self.h = np.zeros(K)   # pamięć (kod ukryty)

        # wagi (inicjalizacja losowa, mała)
        self.W_enc = 0.1 * np.random.randn(K, N)   # encoder: x -> h
        self.W_dec = 0.1 * np.random.randn(N, K)   # decoder: h -> x_hat

    def encode(self, x):
        # enkoder + skręt τ w przestrzeni kodu
        h_lin = self.W_enc @ x
        h = np.tanh(h_lin + self.tau)
        return h

    def decode(self, h):
        # dekoder
        x_hat = np.tanh(self.W_dec @ h)
        return x_hat

    def step(self, x_in, lr=0.001):
        """
        Jeden krok uczenia autoenkodera z pamięcią.
        x_in - wektor wejściowy (N)
        lr   - learning rate
        """

        # wejście + pamięć (TIDER + pamięć)
        x_mix = 0.5 * x_in + 0.5 * self.x

        # enkodowanie (Λ + τ)
        h_new = self.encode(x_mix)

        # pamięć rekurencyjna (h zależy od poprzedniego h)
        h_eff = 0.5 * h_new + 0.5 * self.h

        # dekodowanie
        x_hat = self.decode(h_eff)

        # błąd rekonstrukcji
        err = x_hat - x_in

        # gradient ρ (różnica po pętli)
        rho = np.abs(np.diff(np.concatenate([x_hat, x_hat[:1]])))

        # próg J – aktualizujemy tylko, gdy jest „o co walczyć”
        if np.max(rho) > self.rho_krit:
            # prosta aktualizacja wag (uczenie Hebbowsko‑podobne)
            dW_dec = np.outer(err, h_eff)
            dW_enc = np.outer((self.W_dec.T @ err) * (1 - h_eff**2), x_mix)

            self.W_dec -= lr * dW_dec
            self.W_enc -= lr * dW_enc

        # aktualizacja stanów
        self.x = x_hat
        self.h = h_eff

        return x_hat, err, rho

    def train(self, data, epochs=10, lr=0.001):
        """
        data - tablica [T, N]
        """
        for _ in range(epochs):
            for x_in in data:
                self.step(x_in, lr=lr)

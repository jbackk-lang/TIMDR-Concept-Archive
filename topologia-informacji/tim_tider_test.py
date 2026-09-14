# TIM ↔ TIDER – minimalny eksperyment
# Model pętli z lokalnym skrętem τ i progiem J

import numpy as np
import matplotlib.pyplot as plt

# Parametry układu
N = 100            # liczba węzłów (pętla)
tau = 0.02         # skręt (wymuszenie topologiczne)
rho_krit = 0.3     # próg J (zapłon)
kroki = 500        # liczba iteracji

# Stan początkowy – prawie jednorodny
x = np.zeros(N)
x += 0.001 * np.random.randn(N)

hist = []

for t in range(kroki):
    x_new = np.zeros_like(x)

    # propagacja TIDER
    for i in range(N):
        x_new[i] = np.tanh(x[i-1])   # nieliniowość = sprzężenie

    # skręt τ w jednym miejscu (między N a 1)
    x_new[0] += tau

    # gradient ρ
    rho = np.abs(np.diff(np.concatenate([x_new, x_new[:1]])))

    # punkt zapłonu J
    if np.max(rho) > rho_krit:
        x_new = np.tanh(2 * x_new)   # rezonans po przekroczeniu progu

    x = x_new
    hist.append(x.copy())

# wizualizacja
hist = np.array(hist)
plt.imshow(hist.T, aspect='auto', cmap='inferno')
plt.title("TIM ↔ TIDER – eksperyment")
plt.xlabel("czas")
plt.ylabel("pozycja w pętli")
plt.show()

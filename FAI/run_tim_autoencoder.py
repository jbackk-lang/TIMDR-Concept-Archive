import numpy as np
from tim_autoencoder import TIMAutoencoder

# --- PARAMETRY ---
N = 100      # rozmiar wejścia
K = 16       # rozmiar pamięci / kodu
EPOCHS = 20  # liczba epok
LR = 0.001   # learning rate

# --- GENEROWANIE DANYCH ---
# proste dane: fale sinus + szum
T = 500
data = []
for t in range(T):
    x = np.sin(2 * np.pi * t / 50) * np.ones(N)
    x += 0.05 * np.random.randn(N)
    data.append(x)
data = np.array(data)

# --- INICJALIZACJA MODELU ---
model = TIMAutoencoder(N=N, K=K, tau=0.01, rho_krit=0.2)

# --- TRENING ---
print("Start treningu TIM-Autoencoder...")
for epoch in range(EPOCHS):
    total_err = 0
    for x_in in data:
        x_hat, err, rho = model.step(x_in, lr=LR)
        total_err += np.mean(np.abs(err))
    print(f"Epoka {epoch+1}/{EPOCHS} | błąd: {total_err:.6f}")

print("Trening zakończony.")

# --- TEST ---
test_input = data[0]
x_hat, err, rho = model.step(test_input)

print("\nWejście (fragment):", test_input[:5])
print("Rekonstrukcja (fragment):", x_hat[:5])
print("Błąd (średni):", np.mean(np.abs(err)))

# Równania Modelu Φ

## 1. Prawo skrętu i redukcji

Podstawowe równanie:



\[
R(\tau) = k \cdot \tau^{\,n}
\]



gdzie:  
- \(R(\tau)\) — intensywność redukcji informacji,  
- \(\tau\) — poziom skrętu,  
- \(n\) — wykładnik charakterystyczny dla poziomu (fizyka, biologia, geologia),  
- \(k\) — stała środowiskowa.

---

## 2. Dynamika redukcji w czasie

Zakładamy, że redukcja działa jak „tarcie informacyjne”:



\[
\frac{dI}{dt} = - R(\tau) = -k \cdot \tau^{\,n}
\]



gdzie \(I(t)\) to ilość informacji (złożoności) w układzie.

Jeśli \(\tau\) jest stałe w krótkiej skali czasu:



\[
I(t) = I_0 - k \cdot \tau^{\,n} \cdot t
\]



---

## 3. Sprzężenie skrętu i informacji

Możemy wprowadzić zależność:



\[
\tau = \tau(I)
\]



np. w najprostszym przybliżeniu liniowym:



\[
\tau(I) = a \cdot I
\]



Wtedy:



\[
\frac{dI}{dt} = -k \cdot (aI)^{\,n} = -k a^{\,n} I^{\,n}
\]



co daje równanie typu:



\[
\frac{dI}{dt} = -C \cdot I^{\,n}
\]



z \(C = k a^{\,n}\).

---

## 4. Rozwiązanie potęgowe

Dla \(n \neq 1\):



\[
\int I^{-n} \, dI = -C \int dt
\]





\[
\frac{I^{\,1-n}}{1-n} = -Ct + K
\]





\[
I(t) = \left[(1-n)(K - Ct)\right]^{\frac{1}{1-n}}
\]



To pokazuje, że:

- dla \(n > 1\) redukcja jest szybka na początku i zwalnia z czasem,  
- układ asymptotycznie dąży do stanu minimalnej informacji (φ).

---

## 5. Czas potęgowy

Definiujemy „czas topologiczny”:



\[
T = t^{\,\alpha}
\]



gdzie \(\alpha > 1\) oznacza kompresję historii w obserwowanym czasie.

Możemy wtedy przepisać dynamikę:



\[
\frac{dI}{dT} = \frac{dI}{dt} \cdot \frac{dt}{dT}
\]





\[
\frac{dI}{dT} = -k \cdot \tau^{\,n} \cdot \frac{1}{\alpha} t^{\,1-\alpha}
\]



co pokazuje, że w czasie topologicznym redukcja może być „równomierna”, mimo że w czasie obserwowanym wygląda jak seria gwałtownych skoków (wymierania, przejścia).

---

## 6. Limit φ

Definiujemy stan końcowy jako:



\[
\lim_{t \to \infty} I(t) = I_{\phi}
\]





\[
\lim_{t \to \infty} \tau(t) = 0
\]





\[
\lim_{t \to \infty} R(\tau(t)) = 0
\]



czyli:

- brak skrętu,  
- brak redukcji,  
- czyste φ,  
- tylko stabilna rotacja.

---

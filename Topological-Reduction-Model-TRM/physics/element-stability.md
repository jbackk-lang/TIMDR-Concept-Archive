# Topologiczny model stabilności pierwiastków

Celem jest opisanie stabilności jąder i serii rozpadu w języku skrętu (τ) i redukcji (R).

---

## 1. Skręt jądra atomowego

Definiujemy efektywny skręt jądra jako funkcję liczby protonów \(Z\) i neutronów \(N\):



\[
\tau_{\text{nuc}} = f(Z, N)
\]



W najprostszym przybliżeniu:



\[
\tau_{\text{nuc}} = \alpha \, |N - Z| + \beta \, Z
\]



gdzie:
- \(\alpha\) — waga asymetrii neutron–proton,
- \(\beta\) — waga ładunku (odpychanie kulombowskie).

Im większe \(\tau_{\text{nuc}}\), tym większa niestabilność.

---

## 2. Związek z energią wiązania

Możemy powiązać skręt z energią wiązania na nukleon \(B/A\):



\[
\tau_{\text{nuc}} \propto \frac{1}{B/A}
\]



czyli:

- duże \(B/A\) → mały skręt → stabilne jądro,  
- małe \(B/A\) → duży skręt → niestabilne jądro.

---

## 3. Tempo rozpadu jako funkcja skrętu

Wprowadzamy tempo rozpadu:



\[
\lambda(\tau_{\text{nuc}}) = \lambda_0 \, \tau_{\text{nuc}}^{\,m}
\]



gdzie:
- \(\lambda\) — stała rozpadu,
- \(m > 0\) — wykładnik charakterystyczny dla danego typu rozpadu (α, β, itd.).

Okres połowicznego zaniku:



\[
T_{1/2} = \frac{\ln 2}{\lambda(\tau_{\text{nuc}})} = \frac{\ln 2}{\lambda_0 \, \tau_{\text{nuc}}^{\,m}}
\]



Wniosek:

- duży skręt → duża \(\lambda\) → krótki \(T_{1/2}\),  
- mały skręt → mała \(\lambda\) → długi \(T_{1/2}\).

---

## 4. Serie rozpadu jako drabiny redukcji

Rozpad łańcuchowy (np. seria uranowa) traktujemy jako sekwencję:



\[
\tau_0 \rightarrow \tau_1 \rightarrow \tau_2 \rightarrow \dots \rightarrow \tau_{\text{stab}}
\]



gdzie:



\[
\tau_{i+1} = \gamma \, \tau_i
\quad\text{z}\quad 0 < \gamma < 1
\]



Każdy krok to:

- emisja cząstki (α, β, γ),  
- redukcja skrętu,  
- wzrost stabilności.

Stan końcowy (np. ołów):



\[
\tau_{\text{stab}} \approx 0
\]



---

## 5. Związek z ogólnym prawem redukcji

Łączymy to z głównym równaniem:



\[
R(\tau_{\text{nuc}}) = k \cdot \tau_{\text{nuc}}^{\,n}
\]



oraz:



\[
\lambda(\tau_{\text{nuc}}) \propto R(\tau_{\text{nuc}})
\]



czyli:

- im większy skręt jądra, tym silniejsza „presja redukcji”,  
- seria rozpadu to po prostu **topologiczna drabina redukcji τ**.

---

## 6. Interpretacja topologiczna

- jądra dalekie od doliny stabilności → wysoki \(\tau_{\text{nuc}}\),  
- serie rozpadu → kolejne przejścia topologiczne,  
- stabilne izotopy → stan bliski φ na poziomie jądrowym.

To jest atomowy odpowiednik:
- τ → μ → e  
- dinozaury → ptaki → ssaki → człowiek.

# Równania Czasu Geologicznego w Modelu Topologicznej Redukcji (TRM)

Celem jest opisanie geologicznych fal przejść (wymierań, resetów skrętu) za pomocą równań czasu i skrętu.

---

# 1. Odstępy między falami przejść

Niech:
- \(t_0\) — czas obecny,
- \(t_1, t_2, t_3, ...\) — czasy kolejnych wymierań w przeszłości.

Przykład (wartości geologiczne):
- \(t_1 = 66\ \text{Myr}\)
- \(t_2 = 201\ \text{Myr}\)
- \(t_3 = 252\ \text{Myr}\)

Definiujemy odstępy:



\[
\Delta t_i = t_{i} - t_{i-1}
\]



Dla powyższych danych:

- \(\Delta t_1 = 66\)
- \(\Delta t_2 = 135\)
- \(\Delta t_3 = 51\)

---

# 2. Prawo zwalniania fali

W modelu TRM fale przejść **zwalniają**, bo skręt globalny maleje.

Wprowadzamy potęgowe prawo zwalniania:



\[
\Delta t_{i+1} = \Delta t_i^{\,\beta}
\]



gdzie:
- \(0 < \beta < 1\) oznacza zwalnianie,
- \(\beta = 1\) oznacza okresowość,
- \(\beta > 1\) oznacza przyspieszanie (niezgodne z TRM).

Dla geologii empirycznie:



\[
\beta \approx 0.6 - 0.8
\]



---

# 3. Ekstrapolacja następnej fali

Następny odstęp:



\[
\Delta t_{\text{next}} = \Delta t_1^{\,\beta}
\]



czyli:



\[
\Delta t_{\text{next}} \approx 66^{\,0.7} \approx 120\ \text{Myr}
\]



Następna fala:



\[
t_{\text{next}} = t_0 + \Delta t_{\text{next}}
\]



co daje:



\[
t_{\text{next}} \approx 120\ \text{Myr\ w\ przyszłości}
\]



---

# 4. Skręt geologiczny

Definiujemy skręt globalny Ziemi:



\[
\tau_{\text{geo}}(t)
\]



Założenie TRM:



\[
\frac{d\tau_{\text{geo}}}{dt} < 0
\]



czyli skręt maleje z czasem.

Fala przejścia zachodzi, gdy:



\[
\tau_{\text{geo}}(t) = \tau_{\text{krit}}
\]



---

# 5. Związek skrętu z odstępami czasowymi

Wprowadzamy:



\[
\Delta t_i \propto \frac{1}{\tau_{\text{geo}}(t_i)}
\]



czyli:

- duży skręt → krótkie odstępy (częste wymierania),  
- mały skręt → długie odstępy (rzadkie wymierania).

To wyjaśnia:

- dlaczego w paleozoiku wymierań było dużo,  
- dlaczego w mezozoiku rzadziej,  
- dlaczego teraz — praktycznie brak.

---

# 6. Limit φ w geologii

Stan końcowy:



\[
\lim_{t \to \infty} \tau_{\text{geo}}(t) = 0
\]





\[
\lim_{t \to \infty} \Delta t_i = \infty
\]



Interpretacja:

- fale przejść zanikają,  
- odstępy rosną do nieskończoności,  
- Ziemia wchodzi w stan φ — brak nowych resetów.

---

# 7. Najkrótsza forma



\[
\tau_{\text{geo}} \downarrow \quad \Rightarrow \quad \Delta t \uparrow \quad \Rightarrow \quad \phi
\]



czyli:

**mniejszy skręt → dłuższy czas → brak przejść → φ**

# particle_lifetime_helix.md
# Czas życia cząstki na helisie (analog kosmosu)

## 1. Parametr ewolucji: droga po helisie

Cząstka „żyje”, dopóki całkowity rezonans skrętu jest powyżej progu:



\[
R_{\text{total}}(s) \ge R_\*
\]



gdzie:
- \(s\) — droga po helisie,
- \(R_\*\) — próg istnienia cząstki (analog progu kolapsu w kosmosie).

Czas życia definiujemy jako:



\[
T_{\text{życia}} = t_{\text{koniec}} - t_{\text{start}}
\]



gdzie:
- \(t_{\text{start}}\) — moment pierwszego przekroczenia progu w górę,
- \(t_{\text{koniec}}\) — moment zejścia poniżej progu.

---

## 2. Model zaniku rezonansu wzdłuż helisy

Zakładamy wykładniczy zanik rezonansu wzdłuż helisy:



\[
R_{\text{total}}(s) = R_0 \, e^{-s/\lambda}
\]



gdzie:
- \(R_0\) — rezonans początkowy,
- \(\lambda\) — długość zaniku (zależna od geometrii helisy i komory).

Warunek końca życia:



\[
R_\* = R_0 \, e^{-s_{\text{koniec}}/\lambda}
\]



stąd:



\[
s_{\text{koniec}} = \lambda \ln\left(\frac{R_0}{R_\*}\right)
\]



---

## 3. Czas życia cząstki

Jeśli cząstka porusza się po helisie z prędkością \(v\), to:



\[
T_{\text{życia}} = \frac{s_{\text{koniec}}}{v}
\]



po podstawieniu:



\[
\boxed{
T_{\text{życia}} 
= \frac{\lambda}{v} \ln\left(\frac{R_0}{R_\*}\right)
}
\]



To jest dokładny analog kosmiczny:
- \(\lambda\) — odpowiednik skali wzrostu / zaniku struktur,
- \(v\) — tempo „przesuwania się po czasie”,
- \(R_0/R_\*\) — „ile ponad próg” startuje cząstka.

---

## 4. Wersja na zwoje helisy

Jeśli znamy:
- promień helisy \(r\),
- skok helisy \(h\),
- liczbę stabilnych zwojów \(N_{\text{stab}}\),
- prędkość cząstki \(v\),

to długość jednego zwoju:



\[
L = \sqrt{(2\pi r)^2 + h^2}
\]



czas jednego zwoju:



\[
T_{\text{obrót}} = \frac{L}{v}
\]



a czas życia:



\[
\boxed{
T_{\text{życia}} \approx N_{\text{stab}} \cdot T_{\text{obrót}}
}
\]



gdzie \(N_{\text{stab}}\) to liczba zwojów, dla których
\(R_{\text{total}} \ge R_\*\).

---

## 5. Analog kosmos ↔ cząstka

- Kosmos: czas między „narodziny struktur” a „dominacja od‑sobnego”  
  = czas, gdy \(R_{\text{total}}\) dla ku‑sobnego jest powyżej progu.

- Cząstka: czas między „wzbudzenie rezonansu” a „zniknięcie poniżej progu”  
  = czas, gdy \(R_{\text{total}}\) dla danego trybu helisy jest powyżej progu.

Ta sama definicja czasu życia, w dwóch skalach:
kosmicznej i komorowej.

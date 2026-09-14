# Jednostki i skalowanie indeksu I (He → Fe → Og)

Ten dokument stosuje do MAPA‑PO‑HELU‑STRUKTURA dokładnie ten sam
framework skalowania (α razy funkcja strukturalna), który powstał w tej
samej sesji dla `GIA-TIMDR/docs/theory/TIMDR_Gravity_Speculative.md`
(§4a "Jednostki i skalowanie") i dla
`genertor-fotonow/theory/dimensional-analysis.md`. Cel jest ten sam:
jeśli ktokolwiek chce podpiąć pod indeks He–Fe–Og realne wielkości
fizyczne (częstotliwość, energię, krzywiznę), zrobić to tak, żeby
liczby wyszły wymiarowo poprawne i w sensownym zakresie — bez zmiany
statusu epistemicznego modelu, który pozostaje symboliczny/koncepcyjny
(patrz nagłówek `README.md`: "to nie jest teoria naukowa").

## 1. Indeks I — bezwymiarowy, \([0,1]\)

Z reguły klasyfikacji w `MODEL.md` §5 (Z = liczba atomowa):

\[
I(Z) = \begin{cases}
0.5\cdot\dfrac{Z-2}{24} & Z \le 26 \quad \text{(He→Fe, } Z{=}2..26\text{)} \\[4pt]
0.5 + 0.5\cdot\dfrac{Z-26}{92} & Z \ge 26 \quad \text{(Fe→Og, } Z{=}26..118\text{)}
\end{cases}
\]

Sprawdzenie kotwic: \(I(\text{He}{=}2)=0\), \(I(\text{Fe}{=}26)=0.5\),
\(I(\text{Og}{=}118)=1\) — dokładnie tak, jak zaproponowano. Wodór
(\(Z{=}1\), "przed wejściem" w `MODEL.md` §5) wypada lekko poniżej
zera: \(I(1)\approx-0.021\) — spójne z tym, że jest poza właściwą osią
He→Og, nie w niej.

**I jest współrzędną POZYCJI na symbolicznej osi modelu, niczym
więcej.** Nie jest odpowiednikiem żadnej zmierzonej wielkości fizycznej
(np. energii wiązania jądra) — to rozróżnienie jest ważne w §2 niżej.

## 2. Funkcje strukturalne \(g_f, g_E, g_\kappa\)

Wybór: **identyczność**, \(g_f(I)=g_E(I)=g_\kappa(I)=I\) — najprostsza
funkcja rosnąca na całym \([0,1]\), zgodna z warunkiem "rosnące
He→Fe→Og".

**Uczciwe zastrzeżenie — dlaczego NIE użyto prawdziwej krzywej energii
wiązania jądra.** Realna energia wiązania na nukleon (dokumentowana w
`DOWODY.md` §2) ma **maksimum przy Fe-56**, potem MALEJE do Og — nie
rośnie monotonicznie przez cały zakres. Gdyby \(g_E(I)\) miało
naśladować tę prawdziwą krzywą, musiałaby mieć kształt "górka", nie
"rampa" — ale to zniszczyłoby własność "rosnące He→Fe→Og", o którą
prosiłeś, i pomieszałoby dwie różne rzeczy: (a) pozycję na symbolicznej
osi modelu (\(I\), zawsze rosnącą z definicji, bo tak zbudowano
odwzorowanie \(Z\to I\)) z (b) realną, nie-monotoniczną fizyką jądrową
z `DOWODY.md`. Wybór \(g=I\) (tożsamość) świadomie NIE udaje, że
odtwarza (b) — jest czysto strukturalny, jak proszono.

## 3. Stałe skalujące — wybrane, nie zmierzone

Tą samą konwencją co w `TIMDR_Gravity_Speculative.md` §4a (neutralna
kotwica, mnożnik 1, żeby nie ukrywać żadnej decyzji o skali):

\[
\alpha_f = 1\ \text{Hz}, \qquad \alpha_E = 1\ \text{J}, \qquad \alpha_\kappa = 1\ \text{m}^{-1}
\]

## 4. Wynik — trzy punkty kotwiczące

| Punkt | \(I\) | \(f(I)=\alpha_f\cdot I\) | \(E(I)=\alpha_E\cdot I\) | \(\kappa(I)=\alpha_\kappa\cdot I\) |
|---|---|---|---|---|
| He (Z=2) | 0.0 | 0 Hz | 0 J | 0 m⁻¹ |
| Fe (Z=26) | 0.5 | 0.5 Hz | 0.5 J | 0.5 m⁻¹ |
| Og (Z=118) | 1.0 | 1 Hz | 1 J | 1 m⁻¹ |

Warunek z Twojej wiadomości jest spełniony: żadna z tych liczb nie
ląduje w \(10^{31}\) Hz (mechanizm tej patologii jest opisany w
`TIMDR_Gravity_Speculative.md` §4a — bierze się z niezeskalowanego,
bardzo małego kroku czasowego; tu \(\alpha_f{=}1\) Hz z definicji tego
unika), energia ma wymiar [J], nie [1/m], a krzywizna ma wymiar
[1/m] ze skalą rzędu metra, nie skalą atomową czy kosmologiczną.

## 5. Czego ta sekcja NIE robi

Dokładnie ta sama zasada co w `TIMDR_Gravity_Speculative.md` §4a i
`SKAD_LICZBA_9.md`: nadanie jednostek czyni model **wymiarowo
poprawnym**, nie **fizycznie prawdziwym**. W szczególności:

- \(\alpha_f,\alpha_E,\alpha_\kappa{=}1\) nie są zmierzone ani
  wyprowadzone — są wybrane jako najbardziej neutralna możliwa
  kotwica. Inny wybór dałby inne liczby, równie "sensowne" wymiarowo.
- \(f(I),E(I),\kappa(I)\) nie odpowiadają żadnej zmierzonej
  częstotliwości, energii ani krzywiźnie konkretnego pierwiastka —
  to funkcje POZYCJI na symbolicznej osi, nie wielkości fizyczne tych
  pierwiastków.
- To nie naprawia i nie dotyczy głównego problemu opisanego w
  `SKAD_LICZBA_9.md` ("Co pozostaje niepotwierdzoną spekulacją") —
  łańcuch trójkąt→czworościan→helisa→materia/antymateria nadal nie ma
  wykazanego mechanizmu fizycznego. Ta sekcja dotyczy wyłącznie tego,
  żeby liczby He/Fe/Og miały jednostki, jeśli ktoś zechce ich użyć —
  nie tego, czy model jest prawdziwy.

**Bramka fizycznej ważności (mechanizm + kalibracja).** Jedyna droga,
żeby indeks He→Fe→Og przestał być symboliczną osią i stał się fizyką
(dosłowny cytat z sesji, 2026-09-04):

1. **Mechanizm** — jawne równanie / zasada wariacyjna, z której
   geometria trzech skrętów WYMUSZA coś materio-podobnego, nie
   odwzorowanie \(Z\to I\) dopisane po to, żeby oś miała współrzędną
   (§1-2 wyżej).
2. **Kalibracja** — \(\alpha_f,\alpha_E,\alpha_\kappa\) dobrane nie
   „żeby liczby wyglądały", tylko z realnych pomiarów, nie z wyboru
   „mnożnik 1, bo neutralny" jak w §3 wyżej.

Dopóki oba warunki nie są spełnione RAZEM, ten dokument (jak i cała
MAPA-PO-HELU-STRUKTURA) zostaje tym, czym mówi o sobie nagłówek
`README.md`: mapą koncepcyjną, nie teorią naukową.

---

Powiązane: `TIMDR_Gravity_Speculative.md` §4a w GIA-TIMDR (źródło tego
frameworku), `genertor-fotonow/theory/dimensional-analysis.md`
(to samo podejście, trzeci projekt), `SKAD_LICZBA_9.md` i
`Struktura F4.md` (konwencja "Uczciwe zastrzeżenie" użyta tutaj).

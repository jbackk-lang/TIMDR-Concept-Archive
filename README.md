# TIMDR-Quantum-Lattice — rdzeń wariantu B (zwalidowany)

Podsumowanie ścieżki od `TIMDRQuantumLattice` (kwantowo brzmiący, ale
niezwalidowany szkic) do zweryfikowanego rdzenia z dwoma przetestowanymi
celami predykcyjnymi. Zero danych "na wiarę" — każda liczba niżej pochodzi
z testu, który da się odtworzyć (kod w tym samym folderze).

## Co się nie udało po drodze (i dlaczego to ważne)

- Oryginalny `helix_operator` (`phase + sin(phase)·0.05`) ma punkt stały w
  `π` (pochodna mapy `1−c`, stabilna dla `0<c<2`) — cała siatka kolapsowała
  do jednego, prawie jednorodnego stanu w ~50 krokach, niezależnie od
  ziarna losowego. Sprawdzone empirycznie (4 ziarna → różnica fazy
  ~0.05–0.08 rad po burn-inie) i potwierdzone analitycznie.
- To, nie `defect_operator`, było przyczyną — wyłączenie defektu
  (`temp=0`) nie zapobiegło kolapsowi.
- Oryginalne `Ω = defekt + |rezonans|` nie przewidywało tego, co
  deklarowało (`omega_stability_map` — "predykcja przyszłej stabilności"):
  korelacja z realną przyszłą niestabilnością ≈0, niekonsekwentna w znaku
  na 15 ziarnach.

## Rdzeń — wariant B

**Helisa (H)** — każda komórka ma własną równowagę `eq[x][y]` (losowa,
ustalona przy inicjalizacji), zamiast wspólnego globalnego punktu:

```
twist = sin(eq[x][y] − ϕ) · helix_coef      # helix_coef = 0.05
ϕ' = (ϕ + twist) mod 2π
```

**Defekt (D)** — odległość od WŁASNEJ równowagi, nie od globalnego 0/π.
Gładka, ograniczona wersja (nie liniowa `|wrap(Δ)|`, bo to odtwarzałoby
błąd oryginału z dwoma maksimami — w `eq` i w `eq+π`):

```
Δ = ϕ − eq[x][y]
D(x,y,t) = (1 − cos(Δ)) / 2 · temp          # 0 w eq, temp antypodalnie
```

**Rezonans (R)** — bez zmian względem oryginału, sprzężenie z sąsiadami:

```
R(x,y,t) = sin(avg(sąsiedzi) − ϕ) · 0.1
```

**Test krajobrazu** (burn_in=50–200, 8 ziaren): rozrzut fazy w przestrzeni
ustala się w okolicy 0.28–0.36 (0=kolaps, ~0.9=losowo) — nie zjeżdża do
zera jak oryginał. Trwałość top-10 `D(t)` rośnie z czasem (9.5–9.8/10 przy
burn_in≥50) bez spadku z powrotem przy dłuższym horyzoncie (oryginał przy
burn_in=200 spadał do 2.4/10, bo krajobraz był już całkiem płaski).

## Cel 1: lokalizacja hotspotów — gdzie D będzie największe w `D(t+1)`

15 ziaren, top-10 komórek wg `D(t+1)` jako prawda:

| kandydat | Spearman ρ | top-10 trafień |
|---|---|---|
| **Ω = D(t)** | ≈1.00 | 9.9/10 |
| Ω = D(t) + \|R(t)\| | 0.62–0.76 | 0.3–0.6/10 |

**Ω dla tego celu = D(t).** Dodanie rezonansu nie pomaga, drastycznie
szkodzi (rezonans jest 6–8× większy skalą niż defekt, więc dominuje sumę
i w praktyce zastępuje D(t) czymś, co koreluje z `D(t+1)` dużo słabiej).

## Cel 2: czas do progu — kiedy komórka "osiądzie" blisko `eq`

Zdarzenie: `D(t)` spada poniżej 25 percentyla. 15 ziaren, burn_in=10 (przy
burn_in=50 system już zbyt wolno się rusza, zbyt mało zdarzeń w oknie 40
kroków):

| kandydat | Spearman ρ | top-10 trafień |
|---|---|---|
| Ω = D(t) | 0.63 (0.35–0.86) | 7.1/10 |
| Ω = D(t) + \|R(t)\| | −0.11 (rozstrzelone, znak niestabilny) | 4.0/10 |
| **dystans/tempo zbliżania** (D(t) + wygładzone tempo zmiany, śr. z 5 kroków) | **0.82 (0.69–0.96, wszystkie dodatnie)** | **8.5/10** |

**Ω dla tego celu = D(t) + wygładzone tempo zmiany D**, przeliczone na
`dystans_do_progu / tempo_zbliżania`. To klasyczna ekstrapolacja liniowa
(pozycja + prędkość), nie nowy operator — i to jedyny kandydat, który
faktycznie pobił baseline, konsekwentnie na wszystkich 15 ziarnach.

## Rezonans — status

Dwukrotnie przetestowany jako składnik Ω, na dwóch niezależnych zadaniach.
Za każdym razem pogarszał wynik względem samego D(t). **Pozostaje
oznaczony jako eksperymentalne pole tła** — nie wchodzi do żadnej
oficjalnej definicji Ω, dopóki ktoś nie pokaże zadania, na którym
faktycznie pomaga (nie tylko koreluje w skali całej siatki — to osobno
sprawdzone i też nie wystarcza, bo korelacja masowa nie przekłada się na
trafność w ogonie rozkładu, czyli tam gdzie "hotspot" ma znaczenie).

## Status projektu

Eksploracyjny — cały powyższy wynik to test JEDNEJ konkretnej implementacji
(siatka 10×10, `helix_coef=0.05`, `temp=0.01`, `noise=0.001`), nie ogólne
prawo. Rdzeń (helisa + lokalne eq + defekt względem eq) jest zwalidowany w
tym sensie, że nie kolapsuje i ma dwa działające cele predykcyjne — ale to
nie jest twierdzenie o żadnej fizyce (patrz zastrzeżenie w
`timdr_quantum_lattice_original.py`: to model klasycznych sprzężonych
oscylatorów fazowych, rodzina Kuramoto, nie mechanika kwantowa — nazwy
"kubit"/"dekoherencja"/"splątanie" są kosmetyczne).

## Uruchomienie

```
pip install numpy scipy
python3 test_omega_prediction_variantB.py   # cel 1: lokalizacja hotspotów
python3 test_time_to_threshold.py            # cel 2: czas do progu
python3 sweep_variants.py                    # porownanie original/rotator/local_eq
```

Wszystkie testy są deterministyczne (ziarna 0..N_SEEDS-1) — te same liczby
za każdym uruchomieniem.

## Pliki

- `timdr_quantum_lattice_variants.py` — **kod rdzenia** (tryby `original`,
  `rotator`, `local_eq` w jednej klasie, do porównań/reprodukcji historii
  powyżej). To jest plik, z którego korzystają wszystkie testy poniżej.
- `timdr_quantum_lattice_original.py` — dosłowny, niezmieniony punkt
  wyjścia (kod użytkownika sprzed diagnozy) — zachowany dla historii/
  reprodukcji "co było nie tak".
- `timdr_quantum_lattice_tunable.py` — wersja pośrednia z parametrycznym
  `helix_coef` (użyta w `sweep_dynamics.py` do diagnozy kolapsu, zanim
  powstał wariant B).
- `test_omega_prediction.py` — pierwszy test Ω na ORYGINALE (przed
  naprawą) — pokazuje, skąd wzięła się diagnoza kolapsu.
- `test_omega_prediction_variantB.py` — test celu 1 (lokalizacja
  hotspotów) na zwalidowanym rdzeniu.
- `test_time_to_threshold.py` — test celu 2 (czas do progu).
- `sweep_dynamics.py` — strojenie stałych (`helix_coef`/`temp`/`noise`) na
  oryginalnej formie helisy — pokazuje, że to nie wystarcza.
- `sweep_variants.py` — porównanie `original` / `rotator` / `local_eq` —
  test, który wybrał wariant B.
- `viz_D_omega_D1.html` — wizualizacja D(t)/Ω(t)/D(t+1) z trafieniami
  top-10 (otwórz w przeglądarce).

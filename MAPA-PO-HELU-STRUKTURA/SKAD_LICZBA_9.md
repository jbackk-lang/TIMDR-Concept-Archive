# Skąd bierze się liczba 9 w modelu F4 — pełne podsumowanie

Ten dokument istnieje po to, żeby nikt nie musiał drugi raz przechodzić
przez całą ścieżkę weryfikacji liczby 9 w modelu F4 (`Struktura F4.md`).
Poniżej jest kompletna lista sprawdzonych uzasadnień, dlaczego żadne z
nich nie okazało się niezależnym (matematycznym lub fizycznym) wymogiem,
oraz co z tej analizy zostaje jako realnie wartościowe.

## Krótka odpowiedź

**Liczba 9 jest wyborem modelowym autora, nie wynikiem konieczności
matematycznej ani fizycznej.** Jedyne twarde, sprawdzalne kryterium to:
liczba musi być nieparzysta, żeby warunek balansu `|N+−N-|≤1` miał sens
przy podziale na dwie niemal-równe grupy. To zostawia nieskończenie wiele
kandydatów (3, 5, 7, 9, 11, 13...). Wybór akurat 9 spośród nich opiera się
na subiektywnych, nieskwantyfikowanych ocenach ("nie za mało, nie za
dużo", "w sam raz obliczeniowo") — nie na formule czy progu, który dałoby
się niezależnie wyprowadzić lub sfalsyfikować.

Sama arytmetyka wynikająca z przyjęcia 9 jest poprawna: C(9,4)=C(9,5)=126,
suma 252. Problem nie leży w rachunku — leży w tym, skąd bierze się
wejściowe założenie "9".

## Wszystkie sprawdzone próby uzasadnienia — i dlaczego żadna nie wystarcza

| # | Próba uzasadnienia | Dlaczego nie działa jako niezależny dowód |
|---|---|---|
| 1 | "3 ramiona × 3 pierwiastki (ΔS, τ, Λ) = 9" (oryginalna wersja `Struktura F4.md`) | Opiera się na dwóch dalszych, niewyprowadzonych założeniach: dlaczego akurat 3 ramiona (nie 2 czy 4), i dlaczego akurat 3 "pierwiastki strukturalne" na ramię (nie 2 czy 4) |
| 2 | Helisa o 9 segmentach — "7 ma za mało stopni swobody, 11 ma za dużą degenerację" | Brak zdefiniowanej miary "stopni swobody" i progu, przy którym stają się "wystarczające" |
| 3 | "Nadwartościowość" klas N⁺/N⁻ | Ten sam brak progu co #2, tylko pod nową nazwą — autor sam to później potwierdził wprost |
| 4 | Dualność klas: C(9,4)=C(9,5) | To prawda dla KAŻDEGO n (C(n,k)=C(n,n−k) to podstawowa symetria trójkąta Pascala) — nie wyróżnia 9 spośród 7, 11 czy jakiejkolwiek innej liczby |
| 5 | "Trójkąt Pascala jako fundament geometryczny" | Te same własności (symetria, dualność, hierarchiczność) dotyczą całego trójkąta Pascala, czyli każdego wiersza n — ogólna własność klasy obiektów nie wybiera jednego przedstawiciela |
| 6 | Czworościan (minimalny sympleks 3D) + ruch śrubowy rysujący helisę | Oba fakty są prawdziwe (czworościan ma 4 wierzchołki — to definicja sympleksu 3D; ruch śrubowy realnie rysuje helisę), ale żaden nie tłumaczy, czemu akurat 3/4, ani czemu geometria miałaby oznaczać powstanie materii — to inna kategoria stwierdzeń (kształt trajektorii vs. fizyczne powstanie rzeczy) |
| 7 | "Zbiór 3-elementowy ma tylko jedną strukturę (trójkąt), zbiór 4-elementowy — wiele" | Matematycznie fałszywe: zbiór 3-elementowy ma 4 nieizomorficzne grafy, 5 podziałów (liczba Bella B₃), 512 relacji binarnych — bogatą strukturę, nie jedną |

## Jedyne twarde kryterium, jakie się utrzymało

Liczba musi być **nieparzysta** — to jedyny warunek, który realnie różnicuje
kandydatów (wyklucza liczby parzyste). Ale to wciąż zostawia nieskończony
zbiór możliwości (3, 5, 7, 9, 11...), więc samo to nie tłumaczy wyboru 9.

## Co jest prawdziwe i warte zachowania w dokumentacji

- **Cała arytmetyka F4 jest poprawna:** C(9,4)=126, C(9,5)=126, suma=252,
  podział 126+126. Zweryfikowane niezależnie.
- **Realny, sprawdzalny powód, dla którego hel jest wyjątkowy w budowie
  materii:** luka masy 5 i 8 (nie istnieją stabilne jądra o tych masach
  atomowych) wymusza, że cięższe pierwiastki od węgla wzwyż muszą
  powstawać przez proces potrójny‑alfa (3 jądra helu-4 łączą się naraz
  w węgiel-12, omijając niestabilne masy 5 i 8). To jest prawdziwy,
  policzalny mechanizm — mocniejszy i bardziej konkretny niż ogólnikowe
  "wynika to z właściwości helu" z oryginalnych dokumentów.
- **Poprawka chronologii:** w nukleosyntezie pierwotnej (pierwsze ~20 minut
  po Wielkim Wybuchu) to wodór (wolne protony) powstał first i dominuje
  masowo (~75%), hel-4 (~25%) powstał później, z fuzji protonów i
  neutronów. Hel nie jest chronologicznie "pierwszym pierwiastkiem" — jest
  drugim, ale odgrywa unikalną rolę jako "brama" do cięższych pierwiastków
  (patrz punkt wyżej).
- **118 pierwiastków to aktualna, potwierdzona liczba** (sierpień 2026);
  pierwiastek 119 nie jest jeszcze potwierdzony (trwa wyścig, prowadzi
  RIKEN, Japonia).

## Co pozostaje niepotwierdzoną spekulacją

Cały łańcuch: trójkąt → czworościan → ruch śrubowy → helisa → powstanie
materii → podział na materię/antymaterię → helisy galaktyczne → ciemna
materia w czarnych dziurach. Na żadnym z tych kroków nie pokazano
mechanizmu fizycznego łączącego jeden etap z następnym — to są prawdziwe,
osobne pojęcia (niektóre z realnej geometrii, niektóre z realnej
astrofizyki) połączone przez podobieństwo nazw lub kształtu, nie przez
wspólny wzór czy dane. To może być wartościowa inspiracja koncepcyjna,
ale nie jest to wykazane jako opis rzeczywistości.

## Rekomendacja dla dokumentacji

Wszędzie, gdzie pojawia się liczba 9 jako "wynik" czy "dowód", warto pisać
wprost: **"9 zostało przyjęte jako założenie modelu (nieparzyste,
obliczalne, subiektywnie <<w sam raz>>) — nie zostało wyprowadzone z
niezależnej fizyki ani geometrii helu."** To jest uczciwe wobec czytelnika
i nie umniejsza wartości modelu jako narzędzia koncepcyjnego.

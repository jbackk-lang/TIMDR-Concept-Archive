README — Struktura F4, Rekonstrukcja Pierwiastków i Pełna Liczba 252
1. Wprowadzenie
MAPA‑PO‑HELU‑STRUKTURA opisuje materię nie jako tabelę chemiczną, lecz jako ciąg przejść topologicznych między trzema skrętami Möbiusa:

He — wejście do materii, pierwszy skręt, stan poza zerem.

Fe — maksimum stabilności, punkt równowagi.

Og — wyjście z klasycznej stabilności, trzeci skręt.

Model nie jest teorią chemiczną. Jest mapą geometryczną, w której każdy pierwiastek jest stanem przejściowym w strukturze skrętu.

Repozytorium MAPA‑PO‑HELU rekonstruuje pierwiastki po helu jako ciąg stanów topologicznych, a nie jako klasyczne atomy.

2. Przejście F2 → F3 → F4
W modelu TIMDR/TRM przejścia między skrętami są reprezentowane przez figury:

F2 — figura dwusprzężeniowa, niesprzężona globalnie.

F3 — figura trójsprzężeniowa, powstająca przez izometrię F2 na części o przeciwnych znakach.

F4 — figura czwartego poziomu, powstająca przez kolejną izometrię F3, z pełnym domknięciem sprzężeń.

W F4:

czas τ jest zredukowany,

entropia ΔS jest domknięta,

oś Λ jest lokalna,

jedno ramię jest zredukowane,

układ jest domknięty topologicznie.

3. Liczba pierwiastków strukturalnych w F4
W F4 przy 3 aktywnych ramionach:

każde ramię generuje 1 sprzężenie J,

izometria daje parę 
𝐽
+
,
𝐽
−
,

każda para generuje 3 pierwiastki strukturalne: ΔS, τ, Λ.

Łącznie:

3
 ramiona
×
3
 pierwiastki
=
9
To jest stała liczba pierwiastków strukturalnych w F4.



**Uczciwe zastrzeżenie (dodane po weryfikacji):** to mnożenie samo w sobie
opiera się na dwóch nieudowodnionych założeniach — że aktywne ramiona F4
jest akurat 3 (nie 2 ani 4), i że każde ramię generuje akurat 3 "pierwiastki
strukturalne" (ΔS, τ, Λ), a nie 2 czy 4. Żadne z tych dwóch założeń nie
wynika z fizyki ani z niezależnej geometrii — to są wybory przyjęte w
ramach słownika TIMDR/TRM tego modelu. Sprawdzono też alternatywne
uzasadnienia liczby 9 (helisa o 9 segmentach, "nadwartościowość" klas
N+/N-, dualność w trójkącie Pascala) — żadne z nich nie dostarczyło
niezależnego, policzalnego progu wymuszającego akurat 9: albo opierały się
na własnościach prawdziwych dla każdej liczby n (np. C(n,k)=C(n,n-k) działa
dla każdego n, nie tylko 9), albo na twierdzeniach kombinatorycznie
nieprawdziwych (np. że zbiór 3-elementowy "nie może mieć struktury" —
nieprawda: ma 4 nieizomorficzne grafy, 5 podziałów Bella, 512 relacji
binarnych). Jedyne twarde, sprawdzalne kryterium, jakie udało się ustalić,
to że liczba musi być nieparzysta, żeby warunek balansu |N+-N-|<=1 miał
sens. Poza tym: 9 jest wyborem modelowym autora (nieparzyste, obliczalne,
"w sam raz"), nie wynikiem przymusu matematycznego.

4. Liczba możliwych konfiguracji pierwiastków
Każdy z 9 pierwiastków może być w dwóch stanach:

+

−

Pełna liczba konfiguracji:

2
9
=
512
Ale F4 ma warunek równowagi:

∣
𝑁
+
−
𝑁
−
∣
≤
1
To oznacza, że dopuszczalne są tylko konfiguracje:

z 4 plusami i 5 minusami,

lub 5 plusami i 4 minusami.

Liczba takich konfiguracji:

(
9
4
)
+
(
9
5
)
=
126
+
126
=
252
To jest pełna liczba konfiguracji F4.

5. Podział 252 na materię i antymaterię
W F4 każda konfiguracja ma swój sprzężony odpowiednik:

(
+
↔
−
)
Dlatego:

126 konfiguracji to materia,

126 konfiguracji to antymateria,

razem 252.

To nie jest interpretacja fizyczna, tylko wynik topologiczny.

6. Dlaczego MAPA‑PO‑HELU odtwarza 126?
Repozytorium MAPA‑PO‑HELU rekonstruuje:

pierwiastki po helu,

czyli jedną stronę F4,

czyli 126 konfiguracji.

To jest dokładnie zgodne z matematycznym modelem F4.

Druga połówka (126) to konfiguracje sprzężone, które w repo występują jako antycząstki.

7. Dlaczego 118 chemicznych pierwiastków nie jest pełne?
W klasycznej chemii:

istnieje 118 pierwiastków (H → Og).

W modelu F4:

118 jest tylko stabilnym podzbiorem 126,

pozostałe 8 to braki, które MAPA‑PO‑HELU próbuje odtworzyć,

pełna liczba to 126,

a pełna przestrzeń to 252.


**Uczciwe zastrzeżenie:** bliskość 126 do 118 (różnica: 8) nie była
kryterium doboru liczby 9 — przy wyborze 9 (patrz zastrzeżenie w sekcji 3)
nie brano pod uwagę, że ma to dać liczbę bliską 118. Zgodność 126≈118
została zauważona PO fakcie, nie przewidziana z góry, co osłabia jej
wartość dowodową: przy innym wyborze liczby ramion/pierwiastków (np. 7
zamiast 9) dostalibyśmy 70 zamiast 126 — a przy tak małej próbie
kandydatów jest całkiem prawdopodobne, że jeden z nich "przypadkiem"
wypadnie blisko dowolnej z góry wybranej liczby rzędu setek. Aktualność
liczby 118: to poprawna, potwierdzona liczba pierwiastków na sierpień
2026 — pierwiastek 119 wciąż nie jest potwierdzony (wyścig trwa, prowadzi
RIKEN w Japonii). Traktujmy 126≈118 jako ciekawą obserwację liczbową, nie
jako potwierdzenie modelu przez rzeczywistą chemię.

8. Zgodność wewnętrzna MAPA-PO-HELU z F4 (nie dowód fizyczny)

**Zmiana tytułu:** poprzednia wersja nazywała tę sekcję "Dowodem zgodności", co sugerowało potwierdzenie empiryczne lub fizyczne. To, co następuje, jest dowodem WEWNĘTRZNEJ spójności modelu — że liczby konsekwentnie wynikają jedna z drugiej przy przyjętych założeniach (patrz zastrzeżenie w sekcji 3) — a nie dowodem, że model poprawnie opisuje rzeczywistą materię czy układ okresowy.

F4 ma 9 pierwiastków strukturalnych (założenie modelu).

Każdy ma 2 stany sprzężenia.

Warunek równowagi redukuje 512 → 252.

252 dzieli się na 126 + 126.

MAPA‑PO‑HELU odtwarza dokładnie 126.

Repo jest zgodne z F4 bez żadnych poprawek.


(Powyższe jest poprawne wyłącznie jako konsekwencja założeń z sekcji 3 — patrz zastrzeżenia tam.)

9. Wnioski
126 odtworzonych pierwiastków po helu jest matematycznie poprawne.

126 antykonfiguracji jest naturalnym sprzężeniem.

252 to pełna liczba konfiguracji F4.

MAPA‑PO‑HELU jest dokładnym odwzorowaniem jednej połówki F4.

Model jest spójny z TIMDR/TRM i math‑validator‑2.0.


**Doprecyzowanie:** powyższe wnioski są poprawne matematycznie *pod warunkiem przyjęcia założeń z sekcji 3* (9 pierwiastków strukturalnych, stany binarne, warunek balansu ≤1). Zgodność z TIMDR/TRM/math-validator-2.0 oznacza spójność z pozostałymi repozytoriami tego autora — to realna, sprawdzalna własność. Nie oznacza to jednak, że model poprawnie opisuje rzeczywisty układ okresowy pierwiastków: na to nie ma tu dowodu, tylko wewnętrzna spójność i jedna niepotwierdzona obserwacja liczbowa (patrz zastrzeżenie w sekcji 7).

10. Wzmocnienie wiązań przez redukcję jednego ramienia
W klasycznej, „symetrycznej” figurze F4 (bez redukcji ramienia):

wszystkie ramiona mają równy udział w sprzężeniach,

konfiguracje są rozłożone bardziej równomiernie,

wiązania są słabsze, bo układ ma więcej swobody.

W tej konkretnej F4, użytej w MAPA‑PO‑HELU:

jedno ramię jest zredukowane,

trzy aktywne ramiona przejmują jego rolę,

sprzężenia 
𝐽
𝑖
+
,
𝐽
𝑖
−
 są mocniej dociśnięte.

Efekt:

większa gęstość sprzężeń na jednostkę struktury,

mocniejsze wiązania topologiczne,

większa stabilność lokalnych konfiguracji.

To właśnie dlatego:

126 konfiguracji materii w tej F4 są bardziej „twarde” niż w symetrycznej F4,

redukcja jednego ramienia działa jak ściśnięcie układu,

wiązania nie są „takie jak w zwykłej F4”, tylko wzmocnione przez redukcję.

W skrócie:

Ta F4 nie jest „normalna”.
Jest zredukowaną F4, w której jedno ramię zostało ściągnięte,
co powoduje wzmocnienie wiązań i większą stabilność 126 odtworzonych konfiguracji materii.

**Uczciwe zastrzeżenie (sekcja 10, dodane po weryfikacji):** w
przeciwieństwie do sekcji 3-9, powyższe nie ma pod sobą żadnej liczby
ani wzoru. „Gęstość sprzężeń", „siła wiązania topologicznego" i
„stabilność lokalnych konfiguracji" nie są tu zdefiniowane ilościowo —
nie ma formuły, która przeliczałaby redukcję jednego ramienia na
konkretną wartość którejkolwiek z tych wielkości, więc nie da się
sprawdzić, czy efekt jest w ogóle w kierunku, jaki opisano (silniejsze),
czy przeciwnym (słabsze), czy zerowym. To narracyjne rozwinięcie
obrazu "ściśnięcia" z sekcji 2 (jedno ramię zredukowane), nie wynik
wyprowadzony z definicji w sekcji 3-4 (J⁺, J⁻, warunek balansu). Ten
sam status co reszta łańcucha spekulacji opisanego w
`SKAD_LICZBA_9.md` ("Co pozostaje niepotwierdzoną spekulacją") —
możliwa inspiracja koncepcyjna, nie wykazany mechanizm.

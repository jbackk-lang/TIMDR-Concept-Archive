## Dokumentacja online
https://jbackk-lang.github.io/
TIMDR + Λ–τ–ρ na danych 

# TIMDERA — Społeczny Protokół Informacyjny (v1.0)

> **Uwaga: to jest model koncepcyjny / narzędzie do myślenia, nie teoria naukowa ani model empiryczny.**
> Poniższy opis nie przedstawia ustalonej, zweryfikowanej fizyki, biologii ani historii — to autorska metafora
> służąca do analizy struktur. Nie należy tego traktować jako dowodu na to, jak faktycznie zbudowana jest
> rzeczywistość, ani jako publikacji naukowej w rozumieniu peer review.


## Cel modułu
TIMDERA jest społecznym protokołem informacyjnym, który umożliwia kodowanie i dekodowanie komunikatów w strukturach geometrycznych.

**Sprostowanie:** to NIE jest szyfrowanie kryptograficzne ani narzędzie do omijania cenzury czy prawa autorskiego. Klucz J (`timdera_key.py`) to XOR jednobajtowym ziarnem (256 możliwych wartości — pełny brute-force w ułamku sekundy) plus kompresja zlib. Algorytm jest w całości jawny w tym repozytorium. Nie polegaj na tym systemie, jeśli zależy Ci na realnym bezpieczeństwie, anonimowości albo unikaniu moderacji — do tego służą sprawdzone, audytowane narzędzia kryptograficzne, nie ten protokół.

## Elementy protokołu
- Skręt (Twist) — podstawowa jednostka informacji.
- Warstwy Λ–τ–ρ — struktura, transformacja, defekt.
- Klucz J — kompresja i dekodowanie komunikatu.
- Rytm — kodowanie czasowe.
- Modulacja — zmiana skrętu w czasie.

## Działanie protokołu
### Nadawca
1. Koduje treść w skręcie.
2. Nakłada warstwy Λ–τ–ρ.
3. Moduluje rytmem.
4. Kompresuje kluczem J.
5. Wysyła jako obraz/sygnał.

### Odbiorca
1. Dekompresuje kluczem.
2. Odtwarza warstwy.
3. Demoduluje rytm.
4. Odczytuje komunikat.

### Platforma
Bez znajomości algorytmu i wartości `seed`, surowy wynik wygląda jak nieuporządkowane dane, więc proste wyszukiwanie słów kluczowych na samym zakodowanym sygnale nie zadziała wprost. To NIE jest jednak dowód odporności na wykrycie czy cenzurę: schemat kodowania jest publicznie znany (ten kod źródłowy), przestrzeń kluczy jest bardzo mała, a platforma może wykryć sam fakt używania tego formatu albo złamać kodowanie brute-force'em praktycznie natychmiast.

## Struktura modułu
/timdera_protocol/              — koder/dekoder wiadomości (opisany wyżej)
    timdera_core.py
    timdera_key.py
    timdera_layers.py
    timdera_encoder.py
    timdera_decoder.py
    timdera_rhythm.py
/timdr_sygnaly_spoleczne/       — CELOWO PUSTY: zarezerwowane miejsce na
    __init__.py                  osobny, przyszły moduł wykrywania wzorców
                                  w zachowaniach społecznych (anomalia/
                                  defekt/rezonans/skręt) - patrz docstring
                                  w __init__.py. To NIE jest część kodera i
                                  celowo nigdy nie importuje `timdera_protocol`.
/tests/
    test_timdera_roundtrip.py   — testy round-trip kodera (dodane; wcześniej
                                  repo nie miało żadnych testów)

## Status naprawy (audyt)

- **NAPRAWIONE**: `TIMDERRhythm` (krok "moduluje rytmem" / "demoduluje rytm"
  z sekcji "Działanie protokołu" wyżej) była wcześniej martwym kodem -
  `TIMDERCore.encode()`/`decode()` jej w ogóle nie wywoływały, mimo że
  README opisywało ten krok. `TIMDERCore.attach_rhythm()` (opcjonalne, nie
  łamie wstecznej kompatybilności) włącza pełną, poprawnie odwracalną
  ścieżkę 4-krokową.
- **DODANE**: pierwsze testy w repo (`tests/test_timdera_roundtrip.py`) -
  round-trip z i bez rytmu, w tym test wprost sprawdzający, że różna
  historia rytmu daje różne zakodowane bajty (regresja przeciw poprzedniemu
  martwemu kodowi).
- **DOPRECYZOWANE**: warstwy Λ–τ–ρ (`timdera_layers.py`) to trzy proste,
  odwracalne operacje arytmetyczne, nie realna struktura geometryczna czy
  operator torsji w znaczeniu innych repozytoriów TIMDR - dopisany uczciwy
  komentarz w kodzie, żeby nazwa nie sugerowała więcej, niż kod faktycznie
  robi.

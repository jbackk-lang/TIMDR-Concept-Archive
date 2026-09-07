"""
timdr_sygnaly_spoleczne — CELOWO PUSTY na razie. Zarezerwowane miejsce na
DRUGI, osobny moduł: wykrywanie wzorców w zachowaniach społecznych metodami
TIMDR (anomalia / defekt / rezonans / skręt), NIE rozszerzenie kodera
wiadomości z `timdera_protocol/`.

Dlaczego osobny pakiet, nie rozszerzenie `timdera_protocol/`:
`timdera_protocol` KODUJE i DEKODUJE pojedynczą wiadomość (steganografia
lekka + kompresja) - deterministyczna, odwracalna transformacja jednego
komunikatu. Detekcja wzorców społecznych to zupełnie inne zadanie:
analiza SZEREGU CZASOWEGO zachowań (np. częstość postów, sentyment,
zbieżność aktywności wielu kont w czasie) w poszukiwaniu anomalii - nie ma
tu nic do "zakodowania" ani "zdekodowania". Rozdzielenie na dwa pakiety od
początku (zamiast dopisywania detekcji do `timdera_protocol/`) ma
zagwarantować, że:

1. Zmiany w module detekcji NIGDY nie dotykają plików kodera (a więc nie
   mogą przypadkiem zepsuć testów round-trip w `tests/test_timdera_roundtrip.py`).
2. Nazwy klas/funkcji obu modułów mogą się swobodnie różnić bez kolizji
   (np. `TIMDERLayers` w koderze vs. przyszłe `AnomaliaDetector`/
   `RezonansDetector` tutaj) - nie trzeba prefiksować/przemianowywać
   niczego w `timdera_protocol/`, kiedy ten moduł zacznie powstawać.
3. Dokumentacja obu rzeczy nie miesza się w jednym README - jeśli/kiedy
   ten moduł dostanie realną treść, powinien dostać własny README.md w
   tym katalogu, opisujący WYŁĄCZNIE detekcję, nie protokół kodowania.

Planowane (NIE zaimplementowane jeszcze) odwzorowanie czterech sygnałów
TIMDR na zachowania społeczne, do przetestowania protokołem
pozytywnej/negatywnej kontroli syntetycznej PRZED jakimikolwiek realnymi
danymi (patrz framework TIMDR, sekcja o testowaniu predykcyjności sygnału):

- anomalia — pojedyncza metryka konta (częstość postów, sentyment) poza
  statystycznie "normalnym" zakresem, kalibrowanym z okna BEZ badanego
  zjawiska (nie z okna, które już je zawiera - inaczej próg uczy się z
  samego ekstremum, które ma wykryć).
- defekt — nagły skok tej metryki między kolejnymi oknami czasowymi.
- rezonans — WIELE NIEZALEŻNYCH kont/sygnałów zgłasza anomalię w tym samym
  oknie czasowym jednocześnie (licznik zbieżności w czasie, NIE fizyczny
  oscylator/rezonans w innym znaczeniu tego słowa) - potencjalnie użyteczne
  jako sygnał skoordynowanego zachowania (kampania, brigading), ale to
  wymaga osobnej walidacji na realnych danych, nie założenia z góry.
- skręt — odwrócenie trendu (np. sentymentu) między dwoma kolejnymi oknami,
  większe niż próg wyznaczony z rozrzutu tej metryki.

Żadna z tych czterech rzeczy nie jest jeszcze zaimplementowana w tym
katalogu - to świadomie zarezerwowana przestrzeń nazw, nie martwy kod.
"""

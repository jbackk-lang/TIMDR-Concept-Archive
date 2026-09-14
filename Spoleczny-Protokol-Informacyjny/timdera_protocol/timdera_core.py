class TIMDERCore:
    """
    Rdzeń protokołu TIMDERA.
    Operuje na skręcie, warstwach, modulacji rytmem i kluczu.

    NAPRAWA: README ("Działanie protokołu") opisuje 4 kroki nadawcy
    (skręt -> warstwy Λ-τ-ρ -> modulacja rytmem -> klucz J) i 4 kroki
    odbiorcy (klucz -> warstwy -> demodulacja rytmu -> odczyt), ale ten
    moduł wcześniej w ogóle nie wywoływał `TIMDERRhythm` - realnie
    wykonywał tylko 3 kroki, mimo że README obiecywało 4. `attach_rhythm()`
    jest OPCJONALNE (w odróżnieniu od `attach_layers`/`attach_key`, które są
    wymagane) - żeby nie łamać wstecznie kodu, który już używał
    `TIMDERCore` bez rytmu: bez `attach_rhythm()` `encode`/`decode`
    zachowują się dokładnie jak wcześniej (3 kroki, bez modulacji). Z
    `attach_rhythm()` wykonują pełne 4 kroki z README.

    Okres modulacji (`period`, zwracany przez `TIMDERRhythm.modulate()`)
    jest przenoszony RAZEM z wiadomością (jako pierwsza liczba w danych
    przekazywanych do `key.compress`), nie tylko trzymany w stanie obiektu
    `rhythm` - patrz uzasadnienie w `timdera_rhythm.py`: demodulacja musi
    użyć DOKŁADNIE tego okresu, co modulacja tej konkretnej wiadomości,
    niezależnie od tego, jak zmieniła się historia `rhythm.push()` między
    kodowaniem a dekodowaniem.
    """

    def __init__(self):
        self.layers = None
        self.key = None
        self.rhythm = None

    def attach_layers(self, layers):
        self.layers = layers

    def attach_key(self, key):
        self.key = key

    def attach_rhythm(self, rhythm):
        self.rhythm = rhythm

    def encode(self, data):
        twist = self.layers.apply_structure(data)
        modulated = self.layers.apply_transform(twist)
        defected = self.layers.apply_defect(modulated)
        if self.rhythm is None:
            return self.key.compress(defected)
        rhythm_modulated, period = self.rhythm.modulate(defected)
        return self.key.compress([period] + rhythm_modulated)

    def decode(self, encoded):
        decompressed = self.key.decompress(encoded)
        if self.rhythm is None:
            restored = self.layers.reverse_defect(decompressed)
        else:
            period, *rhythm_modulated = decompressed
            demodulated_rhythm = self.rhythm.demodulate(rhythm_modulated, period)
            restored = self.layers.reverse_defect(demodulated_rhythm)
        demodulated = self.layers.reverse_transform(restored)
        return self.layers.reverse_structure(demodulated)

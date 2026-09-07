import numpy as np


class TIMDERRhythm:
    """
    Rytm — kodowanie czasowe komunikatu.

    NAPRAWA (patrz README, sekcja "Działanie protokołu" - krok 3 "Moduluje
    rytmem" / krok 3 odbiorcy "Demoduluje rytm"): wcześniej ta klasa miała
    tylko `modulate()`, bez odpowiadającego `demodulate()`, i
    `TIMDERCore.encode()`/`decode()` w ogóle jej nie wywoływały - README
    opisywało krok, którego kod nie wykonywał. Teraz `modulate()` zwraca
    JAWNIE użyty okres `period` obok zmodulowanych danych (zamiast go
    ukrywać w stanie obiektu), a `demodulate()` jest jego dokładną
    odwrotnością przy tym samym `period` - dzięki temu `TIMDERCore` może
    przenieść `period` razem z wiadomością (patrz timdera_core.py) i
    poprawnie zdekodować komunikat NIEZALEŻNIE od tego, czy odbiorca ma
    dostęp do tej samej historii `push()` co nadawca. Bez tego demodulacja
    wymagałaby idealnie zsynchronizowanej historii po obu stronach, co jest
    kruche i trudne do przetestowania.
    """

    def __init__(self, history_length=32):
        self.history_length = history_length
        self.history = []

    def push(self, value):
        self.history.append(value)
        if len(self.history) > self.history_length:
            self.history.pop(0)

    def period(self):
        if len(self.history) < 4:
            return None
        fft = np.abs(np.fft.rfft(self.history))
        peak = np.argmax(fft[1:]) + 1
        return int(peak)

    def modulate(self, data):
        """Zwraca (zmodulowane_dane, period) - `period` trzeba przekazać do
        `demodulate()`, żeby odzyskać oryginał (patrz docstring klasy)."""
        p = self.period() or 1
        return [(x + (i % p)) for i, x in enumerate(data)], p

    def demodulate(self, data, period):
        """Dokładna odwrotność `modulate()` przy TYM SAMYM `period`, jakie
        `modulate()` zwróciło przy kodowaniu tej konkretnej wiadomości -
        `period` NIE jest tu ponownie liczone z `self.history`, celowo:
        historia rytmu nadawcy mogła się zmienić (kolejne `push()`) między
        zakodowaniem a zdekodowaniem, więc jedynym wiarygodnym źródłem
        właściwego `period` jest to, co faktycznie zostało użyte przy
        kodowaniu tej wiadomości."""
        p = period or 1
        return [(x - (i % p)) for i, x in enumerate(data)]

"""
test_timdera_roundtrip.py — pierwsze testy w tym repo (wcześniej nie było
ani jednego pliku testowego). Skupione na jednej, krytycznej własności
protokołu TIMDERA: decode(encode(x)) == x, dla każdej ścieżki (z rytmem i
bez), plus test wprost na to, że naprawiona modulacja rytmem faktycznie ma
wpływ na zakodowany wynik (regresja przeciwko wcześniejszemu stanowi, w
którym TIMDERRhythm było martwym kodem - patrz timdera_core.py).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from timdera_protocol.timdera_core import TIMDERCore
from timdera_protocol.timdera_key import TIMDERKey
from timdera_protocol.timdera_layers import TIMDERLayers
from timdera_protocol.timdera_rhythm import TIMDERRhythm
from timdera_protocol.timdera_encoder import TIMDEREncoder
from timdera_protocol.timdera_decoder import TIMDERDecoder


def _core_without_rhythm(seed=1):
    core = TIMDERCore()
    core.attach_layers(TIMDERLayers())
    core.attach_key(TIMDERKey(seed=seed))
    return core


def _core_with_rhythm(seed=1, history=None):
    core = _core_without_rhythm(seed=seed)
    rhythm = TIMDERRhythm()
    for v in (history or []):
        rhythm.push(v)
    core.attach_rhythm(rhythm)
    return core


# ── Bez rytmu (zachowanie sprzed naprawy - musi zostac identyczne) ──────

def test_roundtrip_without_rhythm_ascii_message():
    core = _core_without_rhythm()
    encoder, decoder = TIMDEREncoder(core), TIMDERDecoder(core)
    message = "Hello, TIMDERA!"
    assert decoder.decode_message(encoder.encode_message(message)) == message


def test_roundtrip_without_rhythm_polish_diacritics():
    """ord()/chr() w Pythonie dzialaja na punktach kodowych Unicode, wiec
    polskie znaki (nie tylko ASCII) powinny przejsc bez strat."""
    core = _core_without_rhythm()
    encoder, decoder = TIMDEREncoder(core), TIMDERDecoder(core)
    message = "Zażółć gęślą jaźń"
    assert decoder.decode_message(encoder.encode_message(message)) == message


def test_roundtrip_without_rhythm_empty_message():
    core = _core_without_rhythm()
    encoder, decoder = TIMDEREncoder(core), TIMDERDecoder(core)
    assert decoder.decode_message(encoder.encode_message("")) == ""


def test_roundtrip_without_rhythm_single_char():
    core = _core_without_rhythm()
    encoder, decoder = TIMDEREncoder(core), TIMDERDecoder(core)
    assert decoder.decode_message(encoder.encode_message("A")) == "A"


# ── Z rytmem (naprawiona sciezka - core.py teraz faktycznie wywoluje ────
#    TIMDERRhythm, zgodnie z README "Moduluje rytmem" / "Demoduluje rytm") ──

def test_roundtrip_with_rhythm_default_period_one():
    """Bez wczesniejszych push() (historia < 4) period() zwraca None,
    modulate() uzywa domyslnego period=1 - nadal musi sie poprawnie
    zdekodowac."""
    core = _core_with_rhythm(history=[])
    encoder, decoder = TIMDEREncoder(core), TIMDERDecoder(core)
    message = "no history yet"
    assert decoder.decode_message(encoder.encode_message(message)) == message


def test_roundtrip_with_rhythm_real_period():
    """Historia dajaca >=4 probki -> period() faktycznie liczy FFT i zwraca
    okres != domyslnego 1 (dla tego konkretnego sygnalu okresowego o
    okresie 4) - sprawdzamy NIE TYLKO round-trip, ale i ze period rzeczywiscie
    wyszedl inny niz 1, zeby test nie przeszedl "przypadkiem" przez sam
    fallback."""
    history = [0, 5, 0, 5, 0, 5, 0, 5]  # okres 2
    rhythm_probe = TIMDERRhythm()
    for v in history:
        rhythm_probe.push(v)
    p = rhythm_probe.period()
    assert p is not None and p != 1, "test zaklada okres != domyslnego fallbacku"

    core = _core_with_rhythm(history=history)
    encoder, decoder = TIMDEREncoder(core), TIMDERDecoder(core)
    message = "rhythm with a real period"
    assert decoder.decode_message(encoder.encode_message(message)) == message


def test_rhythm_modulation_actually_changes_encoded_bytes():
    """Regresja wprost przeciwko poprzedniemu stanowi (TIMDERRhythm martwy
    kod, core.encode() go nie wywolywalo): ta sama wiadomosc, ten sam klucz,
    ale RÓŻNA historia rytmu (a wiec rozny period) MUSI dac rozne zakodowane
    bajty - gdyby core.py nadal ignorowalo rhythm, ten test by failowal
    (wynik bylby identyczny niezaleznie od historii)."""
    message = "same message, different rhythm"

    core_a = _core_with_rhythm(history=[0, 5, 0, 5, 0, 5, 0, 5])   # okres 2
    core_b = _core_with_rhythm(history=[0, 0, 5, 5, 0, 0, 5, 5])   # inny ksztalt -> inny okres

    encoded_a = TIMDEREncoder(core_a).encode_message(message)
    encoded_b = TIMDEREncoder(core_b).encode_message(message)
    assert encoded_a != encoded_b


def test_demodulate_is_exact_inverse_of_modulate_for_any_period():
    """Test jednostkowy wprost na TIMDERRhythm, bez reszty pipeline'u -
    demodulate(modulate(data)) == data dla kilku roznych period."""
    data = [10, 20, 30, 40, 50, 5, 15]
    rhythm = TIMDERRhythm()
    for period_hint_history in ([1, 9, 1, 9], [0, 1, 2, 3, 4, 5]):
        r = TIMDERRhythm()
        for v in period_hint_history:
            r.push(v)
        modulated, period = r.modulate(data)
        assert r.demodulate(modulated, period) == data


# ── TIMDERKey - odwracalnosc niezaleznie od rytmu/warstw ────────────────

def test_key_compress_decompress_roundtrip_direct():
    key = TIMDERKey(seed=42)
    data = [0, 1, 2, 127, 128, 300, 100000]
    assert key.decompress(key.compress(data)) == data


def test_key_rejects_negative_numbers_explicitly():
    """_encode_varint rzuca ValueError na ujemne liczby - sprawdzamy, ze to
    NADAL prawda (apply_defect/apply_structure/apply_transform musza
    gwarantowac nieujemnosc na wejsciu do key.compress, wiec to zalozenie
    warte jest jawnego testu, nie tylko domyslnego zaufania)."""
    import pytest
    key = TIMDERKey()
    with pytest.raises(ValueError):
        key.compress([-1])

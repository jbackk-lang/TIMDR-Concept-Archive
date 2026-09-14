import zlib


class TIMDERKey:
    """
    Klucz J — warstwa kompresji i szyfrowania klucza symetrycznego,
    dodawana przy każdym przejściu w protokole TIMDERA.

    NAPRAWA: poprzednia wersja tylko XOR-owała każdy element listy 1:1
    (`[(x ^ self.seed) for x in data]`) i nazywała to "kompresją", mimo że
    rozmiar wyjścia był identyczny jak wejścia — to był szyfr strumieniowy,
    nie kompresja. Ta wersja robi obie rzeczy naprawdę:
      1. koduje liczby jako varint (LEB128) zamiast jednego elementu listy
         na "slot" (oszczędność dla małych wartości, typowych dla kodów
         znaków po warstwach Λ–τ–ρ),
      2. XOR-uje strumień bajtów kluczem `seed` (ta sama rola co wcześniej:
         obfuskacja zależna od klucza),
      3. kompresuje wynik zlib/DEFLATE (level 9) — realna redukcja rozmiaru
         dla typowych, powtarzalnych komunikatów tekstowych.
    Operacja jest w pełni odwracalna: decompress(compress(data)) == data.
    """

    def __init__(self, seed=1):
        self.seed = seed

    def compress(self, data):
        """
        data: iterowalna lista nieujemnych liczb całkowitych.
        Zwraca: bytes (skompresowany, zaszyfrowany blob).
        """
        raw = bytearray()
        for x in data:
            raw += self._encode_varint(int(x))
        key_byte = self.seed & 0xFF
        keyed = bytes(b ^ key_byte for b in raw)
        return zlib.compress(bytes(keyed), level=9)

    def decompress(self, blob):
        """
        blob: bytes zwrócone przez compress().
        Zwraca: lista liczb całkowitych identyczna z wejściem compress().
        """
        keyed = zlib.decompress(blob)
        key_byte = self.seed & 0xFF
        raw = bytes(b ^ key_byte for b in keyed)
        return self._decode_varints(raw)

    def rotate(self):
        self.seed = (self.seed * 3) % 257

    # ── varint (LEB128, bez znaku) ───────────────────────────────────────
    @staticmethod
    def _encode_varint(x: int) -> bytes:
        if x < 0:
            raise ValueError("TIMDERKey.compress obsluguje tylko liczby nieujemne")
        out = bytearray()
        while True:
            byte = x & 0x7F
            x >>= 7
            if x:
                out.append(byte | 0x80)
            else:
                out.append(byte)
                break
        return bytes(out)

    @staticmethod
    def _decode_varints(raw: bytes) -> list:
        values = []
        x = 0
        shift = 0
        for byte in raw:
            x |= (byte & 0x7F) << shift
            if byte & 0x80:
                shift += 7
            else:
                values.append(x)
                x = 0
                shift = 0
        return values

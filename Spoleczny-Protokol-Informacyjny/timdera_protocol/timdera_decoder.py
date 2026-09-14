class TIMDERDecoder:
    """
    Dekodowanie komunikatu przy użyciu klucza i warstw.
    """

    def __init__(self, core):
        self.core = core

    def decode_message(self, encoded):
        data = self.core.decode(encoded)
        return "".join(chr(x) for x in data)

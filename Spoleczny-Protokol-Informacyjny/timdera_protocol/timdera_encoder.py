class TIMDEREncoder:
    """
    Kodowanie komunikatu w skręcie + warstwach + kluczu.
    """

    def __init__(self, core):
        self.core = core

    def encode_message(self, message):
        data = [ord(c) for c in message]
        return self.core.encode(data)

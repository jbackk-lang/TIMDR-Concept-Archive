from orientation import Orientation
from chain import Chain
from resonance import Resonance
from emergence import Emergence

def pipeline(signal):
    o = Orientation()
    c = Chain([signal])
    r = Resonance()
    e = Emergence()

    s1 = o.flip(signal)
    s2 = o.flip(s1)

    if not c.valid():
        return None

    if not r.align(s1, s2):
        return None

    return e.form(True)

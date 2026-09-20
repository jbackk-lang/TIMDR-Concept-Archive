from resonance import Resonance

def test_resonance():
    r = Resonance()
    assert r.align(1, 1)
    assert not r.align(1, 2)

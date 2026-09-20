from orientation import Orientation

def test_orientation():
    o = Orientation()
    assert o.flip(o.flip(1)) == 1

from chain import Chain

def test_chain():
    assert Chain([1, 1]).valid()
    assert not Chain([1, 0]).valid()

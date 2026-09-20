from orientation import Orientation
from chain import Chain
from resonance import Resonance
from emergence import Emergence

o = Orientation()
c = Chain([1])
r = Resonance()
e = Emergence()

s1 = o.flip(1)
s2 = o.flip(s1)

print("Orientation:", s1, s2)
print("Chain valid:", c.valid())
print("Resonance:", r.align(s1, s2))
print("Emergence:", e.form(r.align(s1, s2)))

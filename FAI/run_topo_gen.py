import numpy as np
from tim_topo_generator_double_mem import TIMTopoGeneratorDoubleMem

gen = TIMTopoGeneratorDoubleMem(N=100, K1=32, K2=16, tau1=0.02, tau2=0.01)
seq = gen.generate_sequence(steps=200)

print("Sekwencja wygenerowana. Kształt:", seq.shape)
print("Fragment pierwszego stanu:", seq[0][:10])

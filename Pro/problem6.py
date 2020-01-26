import numpy as np
time_step = 0.02
period = 5
time_vec = np.arange(0, 20, time_step)
print(time_vec)
print(time_vec.size)
sig = np.sin(2 * np.pi / period * time_vec) + 0.5 *np.random.randn(time_vec.size)
print(sig)
print (sig.size)



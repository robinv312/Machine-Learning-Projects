import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,10)
y=x^2
plt.plot(x,y)
plt.title("training")
plt.xlabel("time")
plt.ylabel("distance")
plt.show()
import numpy as np
from matplotlib import pyplot as plt

x = np.array([11,13,14,15,19])
y = np.array([20,21,22,23,24])

plt.xlabel("x")
plt.ylabel("y")

plt.plot(x,y,marker="*", markersize=5)
plt.show()
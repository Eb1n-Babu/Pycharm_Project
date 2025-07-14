import numpy as np
from scipy import stats

speed = list(range(100))

x = np.mean(speed)
y = np.median(speed)
z = stats.mode(speed)
print(x)
print(y)
print(z)
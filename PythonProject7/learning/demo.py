import numpy as np
from matplotlib import pyplot as plt
from numpy import percentile
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = np.mean(speed)
y = np.median(speed)
z = stats.mode(speed)

a = np.std(speed)
b = np.var(speed)
c = np.percentile(speed, 75)
d = np.random.uniform(1,10,10)

plt.plot(d)
plt.show()

print(x)
print(y)
print(z)
print(a)
print(b)
print(c)
print(d)





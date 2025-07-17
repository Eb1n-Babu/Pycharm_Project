import numpy as np
from matplotlib import pyplot as plt

x = np.random.random(100)
print(x)

plt.subplot(2, 1, 1)

plt.hist(x)

y = np.random.random(200)
plt.subplot(2, 1, 2)

plt.hist(y)
plt.show()

a = [5,7,8,7,2,17,2,9,4,11,12,9,6]

b = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.plot(a,b)
plt.show()





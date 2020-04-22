import numpy as np
a = np.arange(3) + 5
print(a)
print('================')
b = np.ones((3,3)) + np.arange(3)
print(b)
print('================')
c = np.arange(3).reshape((3,1)) + np.arange(3)
print(c)

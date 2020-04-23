import numpy as np
#numpy.arange(start, stop, step, dtype)
#numpy.linspace(start, stop, num, endpoint, retstep, dtype)
#numpy.logspace(start, stop, num, endpoint, base, dtype)

# NumPy array from 1 to 19
print(np.arange(1,20,dtype='int32'))

# NumPy array from 1 to 19 with step size 2
print(np.arange(1,20,2,dtype='int8'))

# NumPy array from 1 to 20 with 5 numbers in between
print(np.linspace(1,20,5))

# NumPy array from 10^0 to 10^2 with 10 numbers in log scale
print(np.logspace(0,2,10))
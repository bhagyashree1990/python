import numpy as np
# Code starts here

# initialize NumPy array
array  = np.arange(1,11)

# check dimensions
dim = array.ndim

# reshaped array
reshaped = array.reshape(5,2)
new_dim = reshaped.ndim
# check shape
print(dim)
print(new_dim)
# Code ends here

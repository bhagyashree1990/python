import numpy as np
np.random.seed(21)

# Code starts here

# create random 5x5 array
z = np.random.random((5,5))
# minimum and maximum values
zmax = np.max(z)
zmin = np.min(z)

# normalize
z_norm = ( z - zmin ) / (zmax-zmin)
# display
print(z_norm)
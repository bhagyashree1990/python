#Find roots of quadratic equation

# import packages
import numpy as np

# Code starts here

# co-efficients of x
coeff = np.array([1,-4,4])

# roots of equation
roots = np.roots(coeff)

# display roots
print(roots)
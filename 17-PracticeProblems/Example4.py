#Find a 3x3 Non Singular Matrix
import numpy as np
# initialize array B and Identity matrix
B = np.array([[2,0,-1],[0,2,-1],[-1,0,1]])
I = np.eye(3)

# calculate result
A = 3*I - B
print(A)
# Code ends here
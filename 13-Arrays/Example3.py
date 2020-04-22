import numpy as np
#Creates an uninitialized (arbitrary) array 
a = np.empty((3,4),dtype='int8')
print(a)

print('---')
#Creates a new array of specified size, filled with zeros
b = np.zeros((3,4),dtype='int8')
print(b)

print('---')
#Creates a new array of specified size, filled with ones
c = np.ones((3,4),dtype='int8')
print(c)

print('---')
#Creates a new array of given shape and type, filled with a constant value
d = np.full((2,2),7)
print(d)

print('---')
#Creates a 2-D array with ones on the diagonal and zeros elsewhere
e = np.eye(3)
print(e)
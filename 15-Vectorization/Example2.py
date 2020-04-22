import numpy as np
# element wise square root transform
a = np.array([[1,4,9],[16,25,36]])
print(np.sqrt(a))

# element wise log transform
a = np.array([[1,4,9],[16,25,36]])
print(np.log(a))

#Array comparison
a = np.array([1,2,3,4])
b = np.array([1,2,3,4])
print(np.array_equal(a,b))
b = np.array([5,6,7,8])
print(np.array_equal(a,b))
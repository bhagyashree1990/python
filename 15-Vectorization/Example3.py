import numpy as np
#Axes notation
a = np.array([[1,4,9],[16,25,36]])
# computes sum over columns
print(a.sum(axis=0))
print('==========')

# computes sum over rows
print(a.sum(axis=1))
print('==========')

# computes total sum
print(a.sum())

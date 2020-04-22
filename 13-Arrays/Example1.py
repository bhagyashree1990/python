import numpy as np
# create a 1-dimensional array
a = np.array([1,2,3,4])               
# create a 2-dimensional array
b = np.array([[1,2,3,4], [5,6,7,8]])    
print(a)
print('----')
print(b)
#Shape: tells us how many items are present in each dimension
print('The shape of the array a is ', a.shape)
print('The shape of the array b is ', b.shape)
#Dimensions
print('The dimensions of array a is ', a.ndim)
print('The dimensions of array b is ', b.ndim)
#Size
print('The size of the array a is ', a.size)
print('The size of the array b is ', b.size)
#Datatype
print('The datatype of the array a is ', a.dtype)
print('The datatype of the array b is ', b.dtype)
#Itemsize
print('The number of bytes in each element of the array a is  ', a.itemsize)
print('The number of bytes in each element of the array b is ', b.itemsize)

import numpy as np
#Boolean indexing
a = np.array([[4,7,1],[2,5,7],[7,1,1]])
# Boolean condition for values greater than 3
mask = a > 3
print(mask)

# Masking for the above boolean condition in the array
print(a[mask])

print('-------')
# initialize array
array = np.array([3,4.5,3+5j,0])

# boolean filter
real = np.isreal(array)
real_array = array[real]

# boolean filter
imag = np.iscomplex(array)
imag_array = array[imag]

print(real_array)
print(imag_array)
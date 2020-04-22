import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]])

# Pull out second element of third row
print(a[2][1])
print('==========')
# Pull out first two rows and columns
print(a[:2,:2])
print('==========')
# Pull all elements of the third row
print(a[2,:])

#Subset
a = np.array([10,20,30,40,50])
print(a[2:a.size])
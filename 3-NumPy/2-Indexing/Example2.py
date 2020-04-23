import numpy as np
#Integer array indexing
a=np.array([[1,2],[3,4],[5,6]])

print(a[[0,1,2],[0,1,0]])
print('==========')

print(np.array([a[0,0],a[1,1],a[2,0]]))
print('==========')

print(a[[0,0],[1,1]])
print('==========')

print(np.array([a[0,1],a[0,1]]))
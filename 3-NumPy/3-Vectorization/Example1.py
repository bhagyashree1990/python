import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b=np.array([[10,11,12],[13,14,15],[16,17,18]])

#Vectorized Addition using + or add()
print(a+b)
print('==========')
print(np.add(a,b))

print('==========')
#Vectorized Subtraction using - or subtract()
print(a-b)
print('==========')
print(np.subtract(a,b))

print('==========')
#Vectorized Multiplication using * or multiply()
print(a*b)
print('==========')
print(np.multiply(a,b))

print('==========')
#Vectorized Division using / or divide()
print(a/b)
print('==========')
print(np.divide(a,b))
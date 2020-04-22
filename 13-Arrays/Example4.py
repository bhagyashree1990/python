import numpy as np
#Converting a list to array
a=[1,2,3]
b=np.asarray(a)
print(b)

#Converting tuples into array
a=((1,2),(3,4))
b=np.asarray(a)
print(b)

#create a NumPy ndarray from an iterable
a=np.fromiter([1,2,3,4],dtype='int8')
b=np.fromiter((1,2,3,4),dtype='int8')
c=np.fromiter(range(1,5),dtype='int8')
d=np.fromiter('string',dtype='S50')

print("Array a is ",a)
print("Array b is ",b)
print("Array c is ",c)
print("Array d is ",d)
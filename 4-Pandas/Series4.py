import pandas as pd
#Accessing Data in a Series : By Position
# series of numbers from 11 to 20
ser = pd.Series(data = range(11,21),index=range(10))

# retrieve the first element
print("First element is",ser[0])
print('==========')

#retrieve the first three elements
# ser[:3] -----> first three elements
print("First three elements are",ser[:3].values)
print('==========')

# retrieve index
print(ser.index)
print('==========')

# retrieve data
print(ser.values)
print('==========')
import pandas as pd
#Accessing Data in a Series : By Labels
# series of first five multiples of 10
ser = pd.Series(data = [10,20,30,40,50], index = ['a','b','c','d','e'])

# retrieve value at index 'b'
print("Value at index 'b' is ",ser['b'])
print('==========')

# retrieve value at indexes 'a','c' and 'e'
print("Values at indexes 'a','c' and 'e' are ", ser[['a','c','e']].values)
print('==========')

#retrieve value at index 'f' (not present)
try:
    print("Value at index 'f' is",ser['f'])
except KeyError:
    print("There is no such index")
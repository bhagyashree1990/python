import pandas as pd
#Creating series : From Dictionary
labels = ['a','b','c']
dic = {'b':1,'c':2,'d':3}

# Series without specified labels
print(pd.Series(dic))
print('============')

# Series with specified labels
print(pd.Series(dic, labels))
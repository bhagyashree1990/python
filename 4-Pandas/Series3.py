import pandas as pd
#Creating series : From Scalar
# Scalar number
num = 10

# Series with index ['a','b','c']
print(pd.Series(num,index=['a','b','c']))
print('===============')

# Series with index [0,1,2,3,4]
print(pd.Series(num,index=range(5)))
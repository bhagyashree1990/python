import numpy as np
import pandas as pd
#Creating series : From NumPy ndarray
labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)

print(pd.Series(my_data))
print('==================')
print(pd.Series(my_data,index=labels))
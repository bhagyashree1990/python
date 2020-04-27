import pandas as pd
import numpy as np
#Merging DataFrame
df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['high', 'medium', 'low'] * 3,
                    'price': np.random.randint(0, 15, 9)})

df2 = pd.DataFrame({'product': ['apple', 'orange', 'pine'] * 2,
                    'kilo': ['high', 'low'] * 3,
                    'price': np.random.randint(0, 15, 6)})

merged = pd.merge(left=df1,right=df2,left_on=['fruit','weight'],right_on=['product','kilo'],how='inner',suffixes=['_left', '_right'])
print(merged)                    
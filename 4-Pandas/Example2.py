import pandas as pd

filepath = 'Pokemon2.csv'
#Load the Pokemon dataset
df = pd.read_csv(filepath)
#Creating pivot tables
print(pd.pivot_table(df,index='Type 1',values='Attack',aggfunc='sum'))
#Creating multi-index pivot tables
print(pd.pivot_table(df,index=['Type 1','Type 2'],values='Attack',aggfunc='sum'))

#By default pivot table calculates the mean for the column specified as the argument values inside .pivot_table()
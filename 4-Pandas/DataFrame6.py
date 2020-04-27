import pandas as pd
filepath = 'Pokemon2.csv'
#Load the Pokemon dataset
df = pd.read_csv(filepath)
#Renaming columns
df.rename(columns = {'HP':'Health Points'},inplace=True)
#Dropping columns
df.drop(['#'],inplace=True,axis=1)
#Set index
df.set_index('Name', inplace=True)
print(df)

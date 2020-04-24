#import packages
import pandas as pd
# Create DataFrames : From lists

# list of values (single column)
data = ['Rob','Bobby','John','Danny','Manny']

#construct dataframe with column called 'Name'
df = pd.DataFrame(data, columns = ['Name'])

#display
print(df)

#list of values (two columns)
data =[['Rob',25],['Bobby',30],['John',21],['Danny',32],['Manny',23]]

#construct dataframe with columns called 'Name' and 'Age'
df = pd.DataFrame(data,columns = ['Name','Age'])
print('----------')
print(df)
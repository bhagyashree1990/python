import pandas as pd
#Groupby and Sorting

filepath = 'Pokemon2.csv'
#Load the Pokemon dataset
df = pd.read_csv(filepath)
#Inspecting groups
print(df.groupby('Type 1').groups)
# median value of Attack' across categories of 'Type 1'
print(df.groupby('Type 1')[['Attack']].median())
print(df.groupby('Type 1')[['Attack']].median().sort_values(by='Attack',ascending=False))

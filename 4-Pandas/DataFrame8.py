import pandas as pd
#Exploring Numerical Columns

filepath = 'Pokemon2.csv'
#Load the Pokemon dataset
df = pd.read_csv(filepath)
# Which pokemon has the highest Attack?
df.set_index('Name', inplace=True)
max_attack = df['Attack'].idxmax()
print(max_attack)

print(df.describe())

#Conditional Filtering

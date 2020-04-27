import pandas as pd
#Exploring Categorical Data

filepath = 'Pokemon2.csv'
#Load the Pokemon dataset
df = pd.read_csv(filepath)
# How many different variants of Type 1 are there
type_1 = df['Type 1'].nunique()
print(type_1)

# Different variants of Type 1 pokemon
print(df['Type 1'].unique())

# Counts for different variants of Type 1 pokemons
print(df['Type 1'].value_counts())
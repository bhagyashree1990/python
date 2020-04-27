import pandas as pd

filepath = 'Pokemon2.csv'
#Load the Pokemon dataset
df = pd.read_csv(filepath)

#Groupby task
pokemon_type_avg = df.groupby('Type 1')['Attack'].mean().sort_values(ascending=False)

# Strongest pokemon
strongest_type = pokemon_type_avg.index[0]
print(strongest_type)
# Weakest pokemon
weakest_type  = pokemon_type_avg.index[-1]
print(weakest_type)
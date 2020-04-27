import pandas as pd
import numpy as np
filepath = 'Pokemon2.csv'
#Load the Pokemon dataset
df = pd.read_csv(filepath)

#Groupby task
# Set index name as Name
df.index.name = 'Name'
# Create a subset of "Legendary","Generation","Attack" based on `True` Legendary 
pokemon_stats = df[['Legendary','Generation','Attack']]
pokemon_stats = pokemon_stats[pokemon_stats['Legendary']==True]

# Groupby on data to find highest Legendary pokemon
pokemon_stats_legendary = pokemon_stats.groupby(['Generation','Name'])[['Attack']].agg(np.mean).idxmax()[0]
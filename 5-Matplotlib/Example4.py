#Histogram
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# load data
df = pd.read_csv('Pokemon2.csv')

# Code starts here

# Mean 'Attack' for all Pokemons
mean_attack = np.mean(df['Attack'])

# Mean 'Attack' for Dragon type Pokemons
dragon = df[df['Type 1'] == 'Dragon']
mean_dragon = np.mean(dragon['Attack'])


# Histogram for Dragon type Pokemons
dragon.hist(column='Attack', bins=8, figsize=(10,10))
plt.axvline(x=mean_attack, color='green')
plt.axvline(x=mean_dragon, color='black')
# Display plot
plt.show()
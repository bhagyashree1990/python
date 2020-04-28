#Scatter Plot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# load data
df = pd.read_csv('Pokemon2.csv')

# Conditional filtering for 'Electric' pokemons
electric = df[df['Type 1'] == 'Electric']

# Scatter plot for 'Attack' vs 'HP'
electric.plot.scatter(x='HP', y='Attack')

# Display plot
plt.show()
# Stacked Bar Chart
# Which generation (Generation) has the highest chances of being legendary (Legendary)
import pandas as pd
import matplotlib.pyplot as plt
# load data
df = pd.read_csv('Pokemon2.csv')

# Group Pokemons 
res = df.groupby(['Generation', 'Legendary']).size().unstack()

# Plot Chart
res.plot(kind='bar', stacked=True, figsize=(15,10))

# Display plot
plt.show()
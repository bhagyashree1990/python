#Drawing Multiple Plots
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# load data
df = pd.read_csv('Pokemon2.csv')

# Initialize figure and axes
fig, (ax_1, ax_2) = plt.subplots(1,2, figsize=(20,10))

# Stacked bar-chart representing counts
res = df.groupby(['Type 1', 'Legendary']).size().unstack()
res.plot(kind='bar', stacked=True, ax=ax_1)
ax_1.set_title('Stacked bar-chart with counts')

# Stacked bar-chart representing percentages
new_res = res.fillna(0)
new_res['Total'] = new_res[True] + new_res[False]
new_res[True] = (new_res[True] / new_res['Total']) * 100
new_res[False] = (new_res[False] / new_res['Total']) * 100
new_res.drop('Total', inplace=True, axis=1)
new_res.plot(kind='bar', stacked=True, ax=ax_2)
ax_2.set_title('Stacked bar-chart with percentages')
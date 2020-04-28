#Bar-chart and Anatomy of a Plot
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

# load data
df = pd.read_csv('Pokemon2.csv')

# reset index to 'Name'
df.set_index('Name', inplace=True)

# drop column '#'
df.drop('#', inplace=True, axis=1)

#How many different variants of Type 1 
type_1_data = df['Type 1'].value_counts()

# initialize the figure
plt.figure(figsize=[14,8])

# label the axes
plt.xlabel("Type 1 Pokemon Variants")
plt.ylabel("No of Pokemons")

# title the plot
plt.title("Distribution of pokemon across various Type 1 variants")

# build and show the plot
plt.bar(type_1_data.index,type_1_data)
plt.show()
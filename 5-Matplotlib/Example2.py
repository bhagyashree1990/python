# Line Plots and Plot Customizations
import pandas as pd
import matplotlib.pyplot as plt
# load data
df = pd.read_csv('Pokemon2.csv')
# Code starts here

# Type 1 mean attack points dataframe for every category
type_1 = df.groupby(['Type 1'])[['Attack']].mean()

# Type 2 mean attack points dataframe for every category
type_2 = df.groupby(['Type 2'])[['Attack']].mean()

# Reset index for both dataframes
type_1.reset_index(inplace=True)
type_2.reset_index(inplace=True)
# Merge both dataframes
merged = pd.merge(left=type_1,right=type_2,left_on='Type 1',right_on='Type 2',how='inner')

# Drop 'Type 1' column permanently
merged.drop('Type 1', inplace=True, axis=1)
# Rename column
merged.rename(columns = {'Type 2':'Type'},inplace=True)

# Set size of the figure
plt.figure(figsize=(14,8))

# Line plot for 'Type 1' Pokemon mean attack points
plt.plot(merged['Type'], merged['Attack_x'], color='red')

# Line plot for 'Type 2' Pokemon mean attack points
plt.plot(merged['Type'], merged['Attack_y'], color='blue')

# Setting X-axis label
plt.xlabel('Types')
# Setting Y-axis label
plt.ylabel('Mean Attack Points') 

# Title of the plot
plt.title('Comparison of Mean Attack Points for variants of Type 1 and Type 2')

# Setting Y-axis limit
plt.ylim((45, 120))

# Legend 
plt.legend(labels=['Type1', 'Type 2'])

# Display plot
plt.show()

# Code ends here
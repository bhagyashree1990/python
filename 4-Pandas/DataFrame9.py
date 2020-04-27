import pandas as pd
import numpy as np
#Applying Functions

filepath = 'Pokemon2.csv'
#Load the Pokemon dataset
df = pd.read_csv(filepath)

# minumum value
lower = np.min(df['Attack'])

# maximum value
upper = np.max(df['Attack'])

# range
limit = upper - lower
# mean 
mean = np.mean(df['Attack'])

# function
def standardize(x,x_mean,x_range):
    return (x-x_mean)/x_range

# apply for 'Total' column
print(df['Attack'].apply(lambda x:standardize(x,mean,limit)))

#Convert index containing Pokemon names to upper case letters
#Note: Remember that .apply() cannot be used with index labels
df.set_index('Name', inplace=True)
df.index = df.index.str.upper()


# Convert 'Type 1' to lowercase
df['Type 1'] = df['Type 1'].apply(lambda x: x.lower())
# Convert 'Type 2' to lowercase if present else 
df['Type 2'] = df['Type 2'].apply(lambda x: x.lower() if isinstance(x,str) else None)
print(df.head())
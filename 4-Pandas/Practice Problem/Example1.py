import pandas as pd

filepath = 'Pokemon2.csv'
#Load the Pokemon dataset
df = pd.read_csv(filepath)

#APPLY TASK
# Subset the dataframe of Attack
Special_Attack = df[['Attack']]
# Print first 5 rows
print(Special_Attack.head())
# Create a function attack
def attack(num):
    result = None
    if num < 60:
        result = 'Low Attack'
    elif num > 60:
        result = 'Normal Attack'
    else:
        result = 'Attack'
    return result

# apply attack function on the feature Attack.
print(Special_Attack['Attack'].apply(attack))
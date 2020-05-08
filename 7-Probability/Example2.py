#Which area is the house located in?
# import packages
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
path = 'loan_data_set.csv'
# Load dataframe
df = pd.read_csv(path)

# Display values per class of 'Loan_Status'
print(df['Property_Area'].value_counts())
# Total number of records
total = len(df)

# Probability of Urban houses
p_of_urban = len(df[df['Property_Area'] == 'Urban'])/total
print(p_of_urban)
# Probability of Semiurban houses
p_of_semiurban = len(df[df['Property_Area'] == 'Semiurban'])/total
print(p_of_semiurban)
# Probability of either Urban or Semiurban houses 
p_of_or = p_of_urban + p_of_semiurban
print(p_of_or)
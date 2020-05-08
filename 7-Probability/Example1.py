#Will your loan be approved?
# import packages
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
path = 'loan_data_set.csv'
# Load dataframe
df = pd.read_csv(path)

# Display values per class of 'Loan_Status'
print(df['Loan_Status'].value_counts())

# Total number of rows
total = len(df)

# Number of loan applications accepted
yes = len(df[df['Loan_Status']=='Y'])

# Number of loan applications rejected
no = len(df[df['Loan_Status']=='N'])

# Probability of loan getting accepted
p_of_A = yes/total

# Display probability
print(p_of_A)
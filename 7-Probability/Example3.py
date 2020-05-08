#Does gender affect the probability of getting a loan?
# import packages
import pandas as pd
import matplotlib.pyplot as plt

import numpy as np
path = 'loan_data_set.csv'
# Load dataframe
df = pd.read_csv(path)

# Convert to NumPy arrays
#g = df['Gender'].to_numpy()
#l = df['Loan_Status'].to_numpy()
g = np.array(df['Gender'])
l = np.array(df['Loan_Status'])
# creating pivot table 
table = pd.crosstab(g,l,margins=True,margins_name='Total')
print(table)
# Total male applicants
total_male = table.iloc[1,2]
# Total female applicants
total_female = table.iloc[0,2]
# Total male applicants whose loan applications were accepted
total_male_loan = table.iloc[1,1]
# Total female applicants whose loan applications were accepted
total_female_loan = table.iloc[0,1]
# Probability of loan approval when applicant is male
p_of_ymale = total_male_loan/total_male
# Probability of loan approval when applicant is female
p_of_yfemale = total_female_loan/total_female

print(p_of_ymale)
print(p_of_yfemale)
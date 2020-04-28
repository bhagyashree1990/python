#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load data
path = 'Data.csv'
data = pd.read_csv(path)

property_and_loan = data.groupby(['Property_Area','Loan_Status']).size().unstack()
property_and_loan.plot(kind='bar',stacked=False)
plt.xlabel("Property Area")
plt.ylabel("Loan Status")
plt.xticks(rotation=45)
plt.show()
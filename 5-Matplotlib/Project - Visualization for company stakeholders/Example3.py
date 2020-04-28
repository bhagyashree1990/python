#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load data
path = 'Data.csv'
data = pd.read_csv(path)

education_and_loan = data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar',stacked=True)
plt.xlabel("Education Status")
plt.ylabel("Loan Status")
plt.xticks(rotation=45)
plt.show()
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load data
path = 'Data.csv'
data = pd.read_csv(path)
loan_status  = data['Loan_Status'].value_counts()
plt.bar(loan_status.index,loan_status)
plt.show()
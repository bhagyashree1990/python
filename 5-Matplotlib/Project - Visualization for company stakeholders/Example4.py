#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load data
path = 'Data.csv'
data = pd.read_csv(path)

graduate = data[data['Education']=='Graduate']
not_graduate = data[data['Education']=='Not Graduate']

graduate['LoanAmount'].plot(kind='density', label='Graduate')
not_graduate['LoanAmount'].plot(kind='density', label='Not Graduate')


#Code ends here

#For automatic legend display
plt.legend()
#Purpose vs Loan Defaulting
#Importing header files
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency
from scipy.stats import chi2

path='Test.csv' 
#Code starts here
data = pd.read_csv(path)


#Critical value 
critical_value = chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here
yes = data[data['paid.back.loan'] == 'Yes']['purpose'].value_counts()
no = data[data['paid.back.loan'] == 'No']['purpose'].value_counts()
observed = pd.concat([yes.transpose(),no.transpose()],axis=1,keys=['Yes','No'])
#chi-square test
chi2, p, dof, ex = chi2_contingency(observed)

print(chi2)
print(critical_value)
if chi2 > critical_value:
    inference = 'Reject'
else:
    inference = 'Apply'
print(inference)    
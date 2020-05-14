#Installment vs Loan Defaulting
#Importing header files
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.stats.weightstats import ztest

path='Test.csv' 
#Code starts here
data = pd.read_csv(path)

z_statistic, p_value = ztest(x1=data[data['paid.back.loan']=='No']['installment'],x2=data[data['paid.back.loan']=='Yes']['installment'])
print(z_statistic)
print(p_value)

if p_value < 0.05:
    inference = 'Reject'
else:
    inference = 'Accept'
print(inference)
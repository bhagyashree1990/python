#Small Business Interests
#Importing header files
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.stats.weightstats import ztest

path='Test.csv' 
#Code starts here
data = pd.read_csv(path)

data['int.rate'] = data['int.rate'].map(lambda x: str(x)[:-1])
data['int.rate'] = data['int.rate'].astype(float)/100

z_statistic, p_value = ztest(data[data['purpose']=='small_business']['int.rate'],value=data['int.rate'].mean(),alternative='larger')

if p_value < 0.05:
    inference = 'Reject'
else:
    inference = 'Accept'
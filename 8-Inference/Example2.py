#Is the average Lot.Area less than 1200?
import pandas as pd
from statsmodels.stats.weightstats import ztest

# code starts here
path='Test.csv'
data = pd.read_csv(path)

# apply ztest 
z_statistic, p_value = ztest(data['Lot.Area'],value=1200,alternative='smaller')

# print z statistic and p value
print(z_statistic)
print(p_value)

# check the p-value
if p_value < z_statistic:
    inference = 'Accept'
else:
    inference = 'Reject'
print(inference)
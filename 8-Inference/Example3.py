#t - test
#Is the average sale price same for Family and Alloca condition homes
import pandas as pd
# code starts here
path='Test.csv'
data = pd.read_csv(path)
import scipy
# subset the dataframe
family = data[data['Sale.Condition'] == 'Family']['SalePrice']
alloca = data[data['Sale.Condition'] == 'Alloca']['SalePrice']
# conduct two sample t-test
t_stat, p_value = scipy.stats.mstats.ttest_ind(family,alloca)

# print the results
print('t-statistic = ',t_stat)
print('p-value = ',p_value)

if p_value < t_stat:
    inference = 'Reject'
else:    
    inference = 'Accept'
print(inference)
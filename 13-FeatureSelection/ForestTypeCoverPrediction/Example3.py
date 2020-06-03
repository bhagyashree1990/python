#Closer look towards relationship between different variables
import numpy as np
import seaborn as sns
from Example1 import dataset
upper_threshold = 0.5
lower_threshold = -0.5
# Code Starts Here
subset_train = dataset.iloc[:,:10]
data_corr = subset_train.corr()
sns.heatmap(data_corr,vmax=0.8,square=True)
correlation = data_corr.unstack().sort_values(kind='quicksort')
corr_var_list = correlation[((correlation>upper_threshold) | (correlation<lower_threshold)) & (correlation != 1)]
print(corr_var_list)
# Code ends here
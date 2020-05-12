# Interval Estimates
# import packages
import pandas as pd
import numpy as np
from scipy import stats
import math
path='Test.csv'
# Dataframe
data = pd.read_csv(path)

# Code starts here

# sample size
sample_size = 100

# z-critical Score
z_critical = stats.norm.ppf(q=0.95)

# sampling the dataframe
data_sample = data.sample(n=sample_size, random_state=0)

# finding the mean of the sample
sample_mean = np.mean(data_sample['SalePrice'])

# finding the standard deviation of the population
population_std = data.SalePrice.std()

# finding the margin of error
margin_of_error = z_critical * (population_std / math.sqrt(sample_size))

# finding the confidence interval
# finding the confidence interval
confidence_interval = (sample_mean - margin_of_error,sample_mean + margin_of_error)

# finding the true mean
true_mean = data.SalePrice.mean()
# Code ends here
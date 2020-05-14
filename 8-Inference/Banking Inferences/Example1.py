#Confidence Interval
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  

path='Test.csv'
#Code starts here
data = pd.read_csv(path)
data_sample = data.sample(n=sample_size,random_state=0)
sample_mean = data_sample.installment.mean()
sample_std = data_sample.installment.std()

margin_of_error = z_critical * (sample_std/ math.sqrt(sample_size))

confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)
true_mean = data.installment.mean()
print(true_mean)
print(confidence_interval)


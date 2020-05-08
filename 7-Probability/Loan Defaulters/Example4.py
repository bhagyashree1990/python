#visualization of continuous variable
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path='Test.csv'
df = pd.read_csv(path)
# code starts here
inst_median = np.median(df['installment'])
inst_mean = np.mean(df['installment'])
#print(df.columns.values)
df.hist(column='installment',bins=10,color='b')
df.hist(column='log.annual.inc',bins=10,color='g')
plt.show()
# code ends here
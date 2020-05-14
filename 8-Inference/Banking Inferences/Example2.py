#CLT
#Does the central limit theory hold for the `installment` column?
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

path='Test.csv' 
#Code starts here
data = pd.read_csv(path)
#Different sample sizes to take
sample_size=np.array([20,50,100])

#Code starts here
fig, axes = plt.subplots(3,1, figsize=(20,10))
for i in range(len(sample_size)):
    m=[]    
    for j in range(1000):
        m.append(np.mean(data.sample(n=sample_size[i])['installment']))
    mean_series = pd.Series(m)
    axes[i].hist(mean_series)

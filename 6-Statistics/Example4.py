#Positional Average
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path='AmesHousing.csv'
df = pd.read_csv(path)
mean = np.mean(df['SalePrice'])
#print(mean)
mode = df.SalePrice.mode()
#print(mode)
median = np.median(df['SalePrice'])
#print(median)

df.hist(column='SalePrice',bins=40)
plt.plot([mode]*300, range(300), label='mode')
plt.plot([median]*300, range(300), label='median')
plt.plot([mean]*300, range(300), label='mean')

plt.show()

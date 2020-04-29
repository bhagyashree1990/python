#Histogram
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path='AmesHousing.csv'
df = pd.read_csv(path)
df.hist(column='SalePrice',bins=10)
plt.show()
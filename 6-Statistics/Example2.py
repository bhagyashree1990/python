#Scatter Plot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path='AmesHousing.csv'
df = pd.read_csv(path)

df.plot.scatter(x='SalePrice',y='Garage Area')
plt.show()
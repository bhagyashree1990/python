#Pie Charts
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path='AmesHousing.csv'
df = pd.read_csv(path)

garage = df['Garage Cars'].value_counts()
plt.pie(garage)
plt.show()
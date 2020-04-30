#Range
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path='AmesHousing.csv'
df = pd.read_csv(path)
maximum = np.max(df['SalePrice'])
minimum = np.min(df['SalePrice'])
range = maximum - minimum
print(range)
#Mean Absolute Deviation
#C1:Weight #C2:Mean of C1 #C3:Weight-Mean #C4:absolute(C3) #C5: Mean of C4
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path='AmesHousing.csv'
df = pd.read_csv(path)
mean = np.mean(df['SalePrice'])
distance = [abs(x - mean) for x in df['SalePrice']]
mad = np.mean(distance)
# Standard Deviation and Variance
# C1:Weight #C2:Mean of C1 #C3:Weight-Mean #C4:sqaure(C3) #C5: Mean of C4

# Square root of variance is known as standard deviation.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
path='AmesHousing.csv'
df = pd.read_csv(path)
mean = np.mean(df['SalePrice'])
squared_distance = [abs(x - mean)**2 for x in df['SalePrice']]
sd = math.sqrt(np.mean(squared_distance))
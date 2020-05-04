#Check whether GarageArea is skewed
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
path='AmesHousing.csv'
df = pd.read_csv(path)
df.hist(column='Garage Area',bins=20)
plt.show()
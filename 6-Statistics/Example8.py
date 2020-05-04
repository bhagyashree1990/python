# Coefficient of variation
# cv = (std/mean)*100
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
path='AmesHousing.csv'
df = pd.read_csv(path)
garage_mean = df.GarageArea.mean()
garage_std = df.GarageArea.std()
garage_cv = (garage_std/garage_mean)*100
print(garage_cv)

lot_mean  = df.LotArea.mean()
lot_std = df.LotArea.std()
lot_cv = (lot_std / lot_mean) * 100
print(lot_cv)
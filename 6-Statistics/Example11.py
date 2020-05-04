#Covariance
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
path='AmesHousing.csv'
df = pd.read_csv(path)

new = df[['LotArea','SalePrice']].iloc[:20,:].copy()
mean_lotarea  = new.LotArea.mean()
diff_lotarea = (new['LotArea'] - mean_lotarea)

mean_saleprice = new.SalePrice.mean()
diff_saleprice = (new['SalePrice'] - mean_saleprice)

summation = (diff_lotarea * diff_saleprice).sum()
covariance = summation / new.shape[0]
print(covariance)
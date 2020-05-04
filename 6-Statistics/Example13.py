#Correlation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
path='AmesHousing.csv'
df = pd.read_csv(path)

newdf  = df[['Lot Area','SalePrice']].copy()

# Calulating Pearson correlation coefficient
covariance=newdf.cov().iloc[0,1]
std_LotArea = newdf['Lot Area'].std()
std_SalePrice = newdf.SalePrice.std()
pearson  = covariance / (std_LotArea * std_SalePrice)
print(pearson)

# Calculating Spearman rank correlation coefficient
ranks = newdf.rank(axis=0) 
newdf['d^2']=(ranks['Lot Area']-ranks['SalePrice'])**2
d_square = newdf['d^2'].sum()
n = newdf.shape[0]
spearman = 1 -  (6 * d_square / (n * (n**2 - 1)))
print(spearman)
# Combine into a single dataframe
path='Test.xlsx'
# import packages
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
# Load Offers
offers = pd.read_excel(path,sheet_name=0)
# Load Transactions
transactions = pd.read_excel(path,sheet_name=1)
transactions['n']=1
# Merge dataframes
df = pd.merge(offers,transactions)
# Look at the first 5 rows
print(df.head())

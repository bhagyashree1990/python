# Sneak peek at the dataset

import numpy as np
import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns

# Code starts here
path='Test.csv'
# Load dataframe
df = pd.read_csv(path)
# Look at first five rows
print(df.head())
# Shape of the dataset
print(df.shape)
# Describe numerical columns
print(df.describe())
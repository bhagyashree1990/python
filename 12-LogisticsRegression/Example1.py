# Load the dataset
# import packages
import pandas as pd
import numpy as np
# Code starts here
path = 'Test.csv'
data = pd.read_csv(path)
print(data.shape)
print(data.isnull().sum())
# Code ends here
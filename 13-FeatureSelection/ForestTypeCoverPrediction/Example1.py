# Data loading and statistics
import pandas as pd
from sklearn import preprocessing
#path : File path
# Code starts here
# read the dataset
path = 'Test.csv'
dataset = pd.read_csv(path)
# look at the first five columns
print(dataset.iloc[0,0:5])
# Check if there's any column which is not useful and remove it like the column id
dataset.drop(columns = 'Id', inplace=True)
# check the statistical description
print(dataset.describe())
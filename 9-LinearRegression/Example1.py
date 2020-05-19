# import packages
import pandas as pd
import numpy as np

# Code starts here
path_ames_train='Train.csv'
path_ames_test = 'Test.csv'
# read data
train  = pd.read_csv(path_ames_train)
test = pd.read_csv(path_ames_test)

# split into features and target
X_train, y_train = train.iloc[:,:7], train.iloc[:,7]
X_test, y_test = test.iloc[:,:7], test.iloc[:,7]

# display first five rows of training features and target
print(X_train.head())
print(X_test.head())
# Code ends here
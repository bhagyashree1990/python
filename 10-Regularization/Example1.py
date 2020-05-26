#Add Polynomial Features
import pandas as pd
import numpy as np
import sklearn.model_selection as model_selection

# Code starts here
path='Test.csv'
df = pd.read_csv(path)
X = df.loc[:,df.columns != 'list_price']
y = df['list_price']



X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3, random_state=6)

# Add square and cubic powers of 'GarageScore' to train and test
X_train['GarageScore-2'] = X_train['GarageScore']**2
X_train['GarageScore-3'] = X_train['GarageScore']**3   

X_test['GarageScore-2'] = X_test['GarageScore']**2
X_test['GarageScore-3'] = X_test['GarageScore']**3   

# logarithmic transformation of target
y_train = np.log1p(y_train)
y_test = np.log1p(y_test)

# display first five rows of train and test features
print(X_train.head())
#print(y_train.head())

print(X_test.head())
#print(y_test.head())
# Code ends here
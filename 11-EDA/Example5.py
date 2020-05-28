#Treat missing values
from Example4 import X_train,X_test
# Import packages
from sklearn.impute import SimpleImputer
dict_new = {'Attchd':0,'Detchd':1,'BuiltIn':2,'2Types':3,'CarPort':4,'Basment':5}
X_train['GarageType'] = X_train['GarageType'].map(dict_new)
X_test['GarageType'] = X_test['GarageType'].map(dict_new)

# Custom imputers
mean_imputer = SimpleImputer(strategy='mean')
mode_imputer = SimpleImputer(strategy='most_frequent')
# Code starts here
X_train.drop(['PoolQC'],inplace=True,axis=1)
X_test.drop(['PoolQC'],inplace=True,axis=1)

mode_imputer.fit(X_train[['GarageType']])
X_train['GarageType'] = mode_imputer.transform(X_train[['GarageType']])
X_test['GarageType'] = mode_imputer.transform(X_test[['GarageType']])

mean_imputer.fit(X_train[['LotFrontage']])
X_train['LotFrontage'] = mean_imputer.transform(X_train[['LotFrontage']])
X_test['LotFrontage'] = mean_imputer.transform(X_test[['LotFrontage']])

# Code ends here
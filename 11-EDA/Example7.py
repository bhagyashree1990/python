#Scale your numerical features
# Import packages
from sklearn.preprocessing import MinMaxScaler
from Example5 import X_train,X_test
# numerical columns
num_columns = ['LotFrontage', 'TotalBsmtSF', 'GrLivArea', 'LotArea']


# Code starts here
normalizer = MinMaxScaler()
normalizer.fit(X_train[num_columns])
X_train[num_columns] = normalizer.transform(X_train[num_columns])
X_test[num_columns] = normalizer.transform(X_test[num_columns])
print(X_train.head())
print(X_test.head())
# Code ends here
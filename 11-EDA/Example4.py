#Identify percentage of missing values
from Example3 import train,X_test
# Split into feature and target
X_train, y_train = train.iloc[:,:7], train[['SalePrice']]

# Code starts here
missing_columns = (X_train.isnull().sum()*100)/len(X_train)
mask = missing_columns > 50
columns = missing_columns[mask].index.tolist()
print(columns)

rows_percentage = (1 - (len(X_train.dropna(thresh=5)) / len(X_train)))*100
print(rows_percentage)
# Code ends here
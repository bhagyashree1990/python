# Dealing with missing values
from Example2 import X_train,X_test,y_train,y_test
# Code starts here
X_train.dropna(subset=['YOJ','OCCUPATION'],inplace=True)
X_test.dropna(subset=['YOJ','OCCUPATION'],inplace=True)

# Update index
y_train = y_train[X_train.index]
y_test = y_test[X_test.index]

# fill the missing values for train columns with mean
X_train['AGE'].fillna(X_train['AGE'].mean(),inplace=True)
X_train['CAR_AGE'].fillna(X_train['CAR_AGE'].mean(),inplace=True)
X_train['INCOME'].fillna(X_train['INCOME'].mean(),inplace=True)
X_train['HOME_VAL'].fillna(X_train['HOME_VAL'].mean(),inplace=True)
# fill the missing values for test columns with mean
X_test['AGE'].fillna(X_test['AGE'].mean(),inplace=True)
X_test['CAR_AGE'].fillna(X_test['CAR_AGE'].mean(),inplace=True)
X_test['INCOME'].fillna(X_test['INCOME'].mean(),inplace=True)
X_test['HOME_VAL'].fillna(X_test['HOME_VAL'].mean(),inplace=True)
# Code ends here
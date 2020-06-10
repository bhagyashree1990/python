# Convert Datatypes
from Example1 import X_train,X_test,y_train,y_test
# Code starts here
X_train['INCOME'] = X_train['INCOME'].astype(float)
X_train['HOME_VAL'] = X_train['HOME_VAL'].astype(float)
X_train['BLUEBOOK'] = X_train['BLUEBOOK'].astype(float)
X_train['OLDCLAIM'] = X_train['OLDCLAIM'].astype(float)
X_train['CLM_AMT'] = X_train['CLM_AMT'].astype(float)

X_test['INCOME'] = X_test['INCOME'].astype(float)
X_test['HOME_VAL'] = X_test['HOME_VAL'].astype(float)
X_test['BLUEBOOK'] = X_test['BLUEBOOK'].astype(float)
X_test['OLDCLAIM'] = X_test['OLDCLAIM'].astype(float)
X_test['CLM_AMT'] = X_test['CLM_AMT'].astype(float)

print(X_train.isnull().sum())
print(X_test.isnull().sum())
# Code ends here
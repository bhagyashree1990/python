#Clean Data
from Example1 import X_train,X_test,y_train,y_test
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Code starts here
X_train['TotalCharges'].replace(' ', np.NaN, inplace=True)
X_test['TotalCharges'].replace(' ', np.NaN, inplace=True)
X_train['TotalCharges'] = X_train['TotalCharges'].astype(float)
X_test['TotalCharges'] = X_test['TotalCharges'].astype(float)

#print(X_train['TotalCharges'].mean())
#print(X_test['TotalCharges'].mean())

X_train['TotalCharges'].fillna((X_train['TotalCharges'].mean()), inplace=True)
X_test['TotalCharges'].fillna((X_test['TotalCharges'].mean()), inplace=True)

print(X_train.isnull().sum())
print(X_test.isnull().sum())

cat_cols = X_train.select_dtypes(include='O').columns.tolist()
for x in cat_cols:
    le = LabelEncoder()
    X_train[x] = le.fit_transform(X_train[x])

for x in cat_cols:
    le = LabelEncoder()
    X_test[x] = le.fit_transform(X_test[x])

y_train = y_train.replace({'No':0,'Yes':1})
y_test = y_test.replace({'No':0,'Yes':1})


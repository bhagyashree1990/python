#Encode categorical features `SaleCondition` and `GarageType`
# Import packages
from sklearn.preprocessing import LabelEncoder,LabelBinarizer
from Example7 import X_train,X_test
import pandas as pd
# code starts here
label_encoder = LabelEncoder()
X_train['SaleCondition'] = label_encoder.fit_transform(X_train['SaleCondition'])
X_test['SaleCondition'] = label_encoder.fit_transform(X_test['SaleCondition'])

x_train  = pd.get_dummies(X_train['GarageType'])
x_test  = pd.get_dummies(X_test['GarageType'])

onehot_encoder = LabelBinarizer()
x_train = onehot_encoder.fit_transform(x_train)
x_test = onehot_encoder.fit_transform(x_test)

print(x_train)
print(x_test)
# code ends here
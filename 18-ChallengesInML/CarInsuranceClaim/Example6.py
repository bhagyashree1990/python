# Dealing with Imbalanced data
from Example4 import X_train,X_test,y_train,y_test
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

# code starts here
smote = SMOTE(random_state=9)
X_train,y_train = smote.fit_sample(X_train,y_train)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Code ends here
# Convert the categorical values to numeric value
from Example3 import X_train,X_test,y_train,y_test
from sklearn.preprocessing import LabelEncoder
columns = ["PARENT1","MSTATUS","GENDER","EDUCATION","OCCUPATION","CAR_USE","CAR_TYPE","RED_CAR","REVOKED"]

# Code starts here
for col in columns:
    le = LabelEncoder()
    X_train[col] = le.fit_transform(X_train[col].astype(str))
    X_test[col] = le.fit_transform(X_test[col].astype(str))    
# Code ends here

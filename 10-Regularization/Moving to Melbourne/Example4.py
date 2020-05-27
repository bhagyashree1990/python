#Prediction using Ridge
from Example1 import X_train, X_test, y_train, y_test
from sklearn.metrics import r2_score
from sklearn.linear_model import Ridge
# Code starts here
ridge = Ridge()
ridge.fit(X_train,y_train)
ridge_pred = ridge.predict(X_test)
r2_ridge = r2_score(y_test,ridge_pred)
print(r2_ridge)
# Code ends here
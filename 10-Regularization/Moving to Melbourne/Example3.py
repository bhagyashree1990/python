#Prediction Using Lasso
from Example1 import X_train, X_test, y_train, y_test
from sklearn.metrics import r2_score
from sklearn.linear_model import Lasso
# Code starts here
lasso = Lasso()
lasso.fit(X_train,y_train)
lasso_pred = lasso.predict(X_test)
r2_lasso = r2_score(y_test,lasso_pred)
print(r2_lasso)
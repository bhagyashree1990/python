# Does Lasso Do Better?
# import packages
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
from Example1 import X_train,y_train,X_test,y_test,np
# Code starts here
# instantiate lasso model
lasso  = Lasso()
# fit and predict
lasso.fit(X_train,y_train)
lasso_pred = lasso.predict(X_test)
# calculate RMSE
lasso_rmse = np.sqrt(mean_squared_error(y_test,lasso_pred))
print(lasso_rmse)
# check how many feature coefficients are zero
zero_features = sum(lasso.coef_ == 0)
print(zero_features)
# Code ends here
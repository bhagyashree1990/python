# Does Ridge Do Better?
# import packages
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from Example1 import X_train,y_train,X_test,y_test,np
# Code starts here

# instantiate lasso model
ridge = Ridge()

# fit and predict
ridge.fit(X_train,y_train)
ridge_pred =  ridge.predict(X_test)
# calculate RMSE
ridge_rmse = np.sqrt(mean_squared_error(y_test,ridge_pred))
print(ridge_rmse)

# Code ends here
#Select the Best Model by Cross-Validation Using Grid Search
# import packages
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import Lasso, Ridge
from Example1 import X_train,y_train,X_test,y_test,np
import warnings
warnings.filterwarnings('ignore')

# regularization parameters for grid search
ridge_lambdas = [0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1, 3, 6, 10, 30, 60]
lasso_lambdas = [0.0001, 0.0003, 0.0006, 0.001, 0.003, 0.006, 0.01, 0.03, 0.06, 0.1, 0.3, 0.6, 1]

# Code starts here
# instantiate lasso and ridge models
ridge_model = Ridge()
lasso_model = Lasso()
# grid search on lasso and ridge
ridge_grid = GridSearchCV(estimator=ridge_model,param_grid=dict(alpha=ridge_lambdas))
lasso_grid = GridSearchCV(estimator=lasso_model,param_grid=dict(alpha=lasso_lambdas))
# make predictions 
ridge_grid.fit(X_train,y_train)
lasso_grid.fit(X_train,y_train)
ridge_pred = ridge_grid.predict(X_test)
lasso_pred = lasso_grid.predict(X_test)
ridge_rmse = np.sqrt(mean_squared_error(ridge_pred, y_test))
lasso_rmse = np.sqrt(mean_squared_error(lasso_pred, y_test))
# print out which is better
if lasso_rmse < ridge_rmse:
    best_model = "LASSO"
else:
    best_model = "RIDGE"
print(best_model)
# Code ends here
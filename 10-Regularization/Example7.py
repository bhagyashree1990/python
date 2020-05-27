#Use K-Fold |Cross Validation for Model Selection
# import packages
from sklearn.metrics import make_scorer, mean_squared_error
from sklearn.linear_model import Lasso, Ridge
from sklearn.model_selection import cross_val_score
from Example1 import X_train,y_train,X_test,y_test,np
scorer = make_scorer(mean_squared_error, greater_is_better = False)
# Code starts here
# instantiate L1 and L2
L1 = Lasso()
L2 = Ridge()
# cross validation with L1
rmse_L1 = abs(np.mean(cross_val_score(L1,X_train,y_train,scoring = scorer,cv=10)))
# cross validation with L2
rmse_L2 = abs(np.mean(cross_val_score(L2,X_train,y_train,scoring = scorer,cv=10)))
print(rmse_L1)
print(rmse_L2)
# select best model
if rmse_L1 < rmse_L2:
    Model = L1
else:
    Model = L2
print(Model)
# calculate RMSE on test data
Model.fit(X_train,y_train)
Pred = Model.predict(X_test)
Error = np.sqrt(mean_squared_error(y_test,Pred))
print(Error)
# Code ends here
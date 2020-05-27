#Will You Choose Lasso or Ridge with the Holdout Method?
# import packages
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import Lasso, Ridge
from Example1 import X_train,y_train,X_test,y_test,np
# split into training and validation
train_feat, test_feat, train_tar, test_tar = train_test_split(X_train, y_train, test_size=0.25, random_state=42)
# Code starts here
# initiate lasso and ridge
l1 = Lasso()
l2 = Ridge()
# fit on training
l1.fit(train_feat,train_tar)
l2.fit(train_feat,train_tar)
# make predictions and calculate RMSE on validation data
pred_l1 = l1.predict(test_feat)
pred_l2 = l2.predict(test_feat)

rmse_l1 = np.sqrt(mean_squared_error(test_tar,pred_l1))
rmse_l2 = np.sqrt(mean_squared_error(test_tar,pred_l2))
# select best model
if rmse_l1 < rmse_l2:
    selected_model = l1
else:
    selected_model = l2

# make prediction on test data and calculate RMSE
selected_model_pred = selected_model.predict(X_test)
rmse_selected_model_pred = np.sqrt(mean_squared_error(y_test,selected_model_pred))
print(rmse_selected_model_pred)

# Code ends here
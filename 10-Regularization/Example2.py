# import packages
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from Example1 import X_train,X_test,y_train,y_test,np
# Code starts here

# instantiate and fit model
model = LinearRegression()
model.fit(X_train,y_train)

# make predictions and calculate rmse
preds = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test,preds))
print(rmse)
# Code ends here
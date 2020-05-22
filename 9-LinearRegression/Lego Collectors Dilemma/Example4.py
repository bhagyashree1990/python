#Is my price prediction ok?
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from Example3 import X_train,X_test
from Example1 import y_train,y_test
# Code starts here
regressor = LinearRegression()
regressor.fit(X_train,y_train)
# predict on test features
y_pred  = regressor.predict(X_test)
mse = mean_squared_error(y_test,y_pred)
print(mse)
r2 = r2_score(y_test,y_pred)
print(r2)
# Code ends here
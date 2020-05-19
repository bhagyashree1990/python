# Root mean Square Error (RMSE) is nothing but the square root of the mean/average of the squares of all the errors.
# import packages
from sklearn.metrics import mean_squared_error
from Example4 import y_test,y_pred,np
# Code starts here
rmse = np.sqrt(mean_squared_error(y_test, np.exp(y_pred)))
print(rmse)
# Code ends here
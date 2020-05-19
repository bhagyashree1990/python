# Mean absolute error is nothing but the average of absolute values of these residuals. 
# import packages
from sklearn.metrics import mean_absolute_error
from Example1 import y_test
from Example3 import y_pred,np
# Code starts here

# MAE calculation
mae = mean_absolute_error(y_test, np.exp(y_pred))
print(mae)
# Code ends here
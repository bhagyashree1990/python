# Calculate R-squared score
# import packages
from sklearn.metrics import r2_score
from Example4 import y_test,y_pred,np
# Code starts here

# R-squared calculation
rsquared  = r2_score(y_test,np.exp(y_pred))
print(rsquared)
# Code ends here
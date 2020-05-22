#Residual check!
from Example4 import y_test, y_pred
from Example2 import plt
# Code starts here
residual = y_test - y_pred
plt.hist(residual)
# Code ends here
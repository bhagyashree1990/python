#Eliminate skewness from `SalePrice`
# import packages
import seaborn as sns
from Example1 import  y_train, np
# Code starts here
y_train = np.log(y_train)
sns.distplot(y_train)
# Code ends here
#Correlation Check !
import seaborn as sns
from Example1 import X_train
# Code starts here
relation = X_train.corr()
print(relation)
sns.pairplot(X_train)
# Code ends here
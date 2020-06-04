# Decision Tree Pruning
#Importing header files
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier 
from Example1 import X_train,y_train,X_test,y_test
import numpy as np
#Parameter grid
parameter_grid = {'max_depth': np.arange(3,10), 'min_samples_leaf': range(10,50,10)}
# Code starts here
model_2 = DecisionTreeClassifier(random_state=0)
p_tree = GridSearchCV(estimator=model_2,param_grid=parameter_grid,cv=5)
p_tree.fit(X_train,y_train)
acc_2 = p_tree.score(X_test,y_test)
print(acc_2)
# Code ends here
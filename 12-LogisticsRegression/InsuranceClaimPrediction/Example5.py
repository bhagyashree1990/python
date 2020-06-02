#Is my Insurance claim prediction right?
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from Example1 import X_train,y_train,X_test,y_test
# parameters for grid search
parameters = {'C':[0.1,0.5,1,5]}
# Code starts here
lr = LogisticRegression(random_state=9)
grid = GridSearchCV(estimator=lr,param_grid=parameters)
grid.fit(X_train,y_train)
y_pred = grid.predict(X_test)
accuracy = accuracy_score(y_test,y_pred)
print(accuracy)
# Code ends here
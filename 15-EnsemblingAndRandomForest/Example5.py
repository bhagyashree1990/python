# Using Grid Search for Random Forest
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from Example1 import X_train,X_test,y_train,y_test
#Parameter grid
parameter_grid = {"max_depth": [3, None],
              "max_features": [1, 3, 10],
              "min_samples_split": [2, 3, 10],
              "min_samples_leaf": [1, 3, 10],
              "bootstrap": [True, False],
              "criterion": ["gini", "entropy"]}
# Code starts here
clf = RandomForestClassifier(random_state=0)
grid_search = GridSearchCV(estimator=clf,param_grid=parameter_grid)
grid_search.fit(X_train,y_train)
score_gs = grid_search.score(X_test,y_test)
print(score_gs)
# Code ends here
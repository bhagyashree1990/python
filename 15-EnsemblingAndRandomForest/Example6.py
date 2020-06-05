# Using Randomized Search for Random Forest
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from Example1 import X_train,X_test,y_train,y_test
from Example5 import parameter_grid
# Code starts here
clf = RandomForestClassifier(random_state=0)
random_search = RandomizedSearchCV(estimator=clf,param_distributions =parameter_grid,n_iter=20 ,random_state=0)
random_search.fit(X_train,y_train)
score_rs = random_search.score(X_test,y_test)
print(score_rs)
# Code ends here
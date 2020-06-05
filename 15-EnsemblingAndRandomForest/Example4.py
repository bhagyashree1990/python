# Random Forest
from sklearn.ensemble import RandomForestClassifier
from Example1 import X_train,X_test,y_train,y_test
# Code starts here
rf_clf = RandomForestClassifier(n_estimators=100,n_jobs=100, min_samples_leaf=100,random_state=0)
rf_clf.fit(X_train,y_train)
score_rf = rf_clf.score(X_test,y_test)
print(score_rf)
# Code ends here
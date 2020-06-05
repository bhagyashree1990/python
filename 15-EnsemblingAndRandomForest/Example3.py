# Using pasting for prediction
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from Example1 import X_train,X_test,y_train,y_test
# Code starts here
pasting_clf = BaggingClassifier(base_estimator=DecisionTreeClassifier(),n_estimators=100,max_samples=100,bootstrap = False,random_state=0)
pasting_clf.fit(X_train,y_train)
score_pasting = pasting_clf.score(X_test,y_test)
print(score_pasting)
# Code ends here
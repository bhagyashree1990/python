#Bagging or Bootstrap aggregation
# Import Bagging Classifier
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier 
from Example1 import X_train,X_test,y_train,y_test
# Code starts here

bagging_clf = BaggingClassifier(base_estimator= DecisionTreeClassifier(), n_estimators=100 , max_samples=100,random_state=0)
bagging_clf.fit(X_train,y_train)
score_bagging = bagging_clf.score(X_test,y_test)
print(score_bagging)
# Code ends here
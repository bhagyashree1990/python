# Gradient Boosting Implementation
from sklearn.ensemble import GradientBoostingClassifier
from Example1 import X_train,X_test,y_train,y_test
gb_clf  = GradientBoostingClassifier(random_state=0)
gb_clf.fit(X_train,y_train)
gb_score = gb_clf.score(X_test,y_test)
print(gb_score)
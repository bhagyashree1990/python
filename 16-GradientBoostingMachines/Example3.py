# XGBoost Implementation
from xgboost import XGBClassifier
from Example1 import X_train,X_test,y_train,y_test,dt_clf
xgb_clf = XGBClassifier(base_estimator=dt_clf,random_state=0)
xgb_clf.fit(X_train,y_train)
xgb_score = xgb_clf.score(X_test,y_test)
print(xgb_score)
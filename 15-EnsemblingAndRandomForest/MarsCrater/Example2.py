# Predict the values after building a Machine learning model
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from Example1 import X_train,X_test,y_train,y_test
# Code starts here
lr = LogisticRegression()
lr.fit(X_train,y_train)
y_pred = lr.predict(X_test)
roc_score = roc_auc_score(y_test,y_pred)
print(roc_score)
#Code ends here
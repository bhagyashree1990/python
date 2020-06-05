# Decision Tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score
from Example1 import X_train,X_test,y_train,y_test
#Code starts here
dt = DecisionTreeClassifier(random_state=4)
dt.fit(X_train,y_train)
y_pred = dt.predict(X_test)
roc_score = roc_auc_score(y_test,y_pred)
print(roc_score)
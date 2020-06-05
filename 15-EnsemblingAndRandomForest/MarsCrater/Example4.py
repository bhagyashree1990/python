# Can we improve our model's performance with Random forrest algorithm?
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from Example1 import X_train,X_test,y_train,y_test
#Code starts here
rfc = RandomForestClassifier(random_state=4)
rfc.fit(X_train,y_train)
y_pred = rfc.predict(X_test)
roc_score = roc_auc_score(y_test,y_pred)
print(roc_score)
# Code ends here
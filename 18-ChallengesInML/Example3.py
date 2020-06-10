# Cluster Centroids
from imblearn.under_sampling import ClusterCentroids
from Example1 import LogisticRegression,recall_score,precision_score,f1_score,confusion_matrix
from Example1 import X_train,X_test,y_train,y_test
# Code starts here
cc = ClusterCentroids(random_state=0)
X_sample3,y_sample3 = cc.fit_sample(X_train,y_train)
model_cc = LogisticRegression(random_state=0)
model_cc.fit(X_sample3,y_sample3)
y_pred = model_cc.predict(X_test)

accuracy_cc = model_cc.score(X_test,y_test)
recall_cc = recall_score(y_test,y_pred)
precision_cc =  precision_score(y_test,y_pred)
f1_cc = f1_score(y_test,y_pred)
confusion_mat_cc = confusion_matrix(y_test,y_pred)
print('Accuracy',accuracy_cc)
print('Recall',recall_cc)
print('Precision',precision_cc)
print('F1 Score',f1_cc)
print('CF',confusion_mat_cc)
# Code ends here
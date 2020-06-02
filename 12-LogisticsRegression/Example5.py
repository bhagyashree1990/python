# Accuracy score, Precision, Recall and F score
# Accuracy= (TP+TN)/(TP+FP+TN+FN)
# It is a relatively good metric where we have a symmetric distribution of the targets.
# Precision(P)= TP/(TP+FP)
# It is a good measure to determine when the costs of False Positive is high.
# Recall(R)= TP/ (TP+FN)
# It shall be the model metric we use to select our best model when there is a high cost associated with False Negative.
# Fscore= 2PR/(P+R​)
# If you want to achieve a balance between precision and recall, use the Fscore

# import packages
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from Example4 import y_test,y_pred
# Code starts here
cf = confusion_matrix(y_test,y_pred)
acc = accuracy_score(y_test,y_pred)
precision= precision_score(y_test,y_pred)
recall= recall_score(y_test,y_pred)
f_score=f1_score(y_test,y_pred)
# Code starts here
#ROC-AUC score: Calculate AUC
# import packages
from sklearn.metrics import roc_auc_score
from Example4 import y_test,y_pred
roc = roc_auc_score(y_test,y_pred)
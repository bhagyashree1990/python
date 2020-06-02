#Performance of a classifier !
from sklearn.metrics import roc_auc_score
from sklearn import metrics
from Example5 import X_test,y_test,y_pred,grid
import matplotlib.pyplot as plt
# Code starts here
score = roc_auc_score(y_test,y_pred)
y_pred_proba = grid.predict_proba(X_test)[:,1]
fpr, tpr, _ = metrics.roc_curve(y_test,y_pred_proba)
roc_auc = roc_auc_score(y_test,y_pred_proba)
plt.plot(fpr,tpr,label="Logistic model ,auc="+str(roc_auc))
# Code ends here
# Tomek Undersampling
from imblearn.under_sampling import TomekLinks
from Example1 import LogisticRegression,recall_score,precision_score,f1_score,confusion_matrix
from Example1 import X_train,X_test,y_train,y_test
#Code starts here
tl = TomekLinks()
X_sample4,y_sample4 = tl.fit_sample(X_train,y_train)
model_tl = LogisticRegression(random_state=0)
model_tl.fit(X_sample4,y_sample4)
y_pred = model_tl.predict(X_test)

accuracy_tl = model_tl.score(X_test,y_test)
recall_tl = recall_score(y_test,y_pred)
precision_tl =  precision_score(y_test,y_pred)
f1_tl = f1_score(y_test,y_pred)
confusion_mat_tl = confusion_matrix(y_test,y_pred)
print('Accuracy',accuracy_tl)
print('Recall',recall_tl)
print('Precision',precision_tl)
print('F1 Score',f1_tl)
print('CF',confusion_mat_tl)
#Code ends here
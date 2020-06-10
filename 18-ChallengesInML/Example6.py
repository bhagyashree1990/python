# SMOTE (Synthetic Minority Oversampling Technique)
from imblearn.over_sampling import SMOTE
from Example1 import LogisticRegression,recall_score,precision_score,f1_score,confusion_matrix
from Example1 import X_train,X_test,y_train,y_test

# Code starts here
smote = SMOTE(random_state=0)
X_sample6,y_sample6 = smote.fit_sample(X_train,y_train)
model_smote = LogisticRegression(random_state=0)
model_smote.fit(X_sample6,y_sample6)
y_pred  = model_smote.predict(X_test)
accuracy_smote = model_smote.score(X_test,y_test)
recall_smote = recall_score(y_test,y_pred)
precision_smote =  precision_score(y_test,y_pred)
f1_smote = f1_score(y_test,y_pred)
confusion_mat_smote = confusion_matrix(y_test,y_pred)
print('Accuracy',accuracy_smote)
print('Recall',recall_smote)
print('Precision',precision_smote)
print('F1 Score',f1_smote)
print('CF',confusion_mat_smote)

# Code ends here
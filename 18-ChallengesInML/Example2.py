# Random Undersampling
from imblearn.under_sampling import RandomUnderSampler
from Example1 import LogisticRegression,recall_score,precision_score,f1_score,confusion_matrix
from Example1 import X_train,X_test,y_train,y_test
# Code starts here
rus = RandomUnderSampler(random_state=0)
X_sample2,y_sample2 = rus.fit_sample(X_train,y_train)
model_rus = LogisticRegression(random_state=0)
model_rus.fit(X_sample2,y_sample2)
y_pred = model_rus.predict(X_test)
accuracy_rus = model_rus.score(X_test,y_test)
recall_rus = recall_score(y_test,y_pred)
precision_rus =  precision_score(y_test,y_pred)
f1_rus = f1_score(y_test,y_pred)
confusion_mat_rus = confusion_matrix(y_test,y_pred)
print('Accuracy',accuracy_rus)
print('Recall',recall_rus)
print('Precision',precision_rus)
print('F1 Score',f1_rus)
print('CF',confusion_mat_rus)
# Code ends here
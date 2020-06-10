# Random Oversampling
from imblearn.over_sampling import RandomOverSampler
from Example1 import LogisticRegression,recall_score,precision_score,f1_score,confusion_matrix
from Example1 import X_train,X_test,y_train,y_test
# Code starts here
ros = RandomOverSampler(random_state=0)
X_sample5,y_sample5 = ros.fit_sample(X_train,y_train)
model_ros = LogisticRegression(random_state=0)
model_ros.fit(X_sample5,y_sample5)
y_pred = model_ros.predict(X_test)
accuracy_ros = model_ros.score(X_test,y_test)
recall_ros = recall_score(y_test,y_pred)
precision_ros =  precision_score(y_test,y_pred)
f1_ros = f1_score(y_test,y_pred)
confusion_mat_ros = confusion_matrix(y_test,y_pred)
print('Accuracy',accuracy_ros)
print('Recall',recall_ros)
print('Precision',precision_ros)
print('F1 Score',f1_ros)
print('CF',confusion_mat_ros)

# Code ends here
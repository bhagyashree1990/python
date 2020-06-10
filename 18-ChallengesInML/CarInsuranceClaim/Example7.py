# Prediction Check after dealing with imbalanced data
from Example6 import X_train,X_test,y_train,y_test
from Example5 import LogisticRegression,accuracy_score
# Code Starts here
model = LogisticRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
score = accuracy_score(y_test,y_pred)
print('Accuracy',score)
# Code ends here
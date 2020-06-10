# Prediction check
from Example4 import X_train,X_test,y_train,y_test
from sklearn.metrics import precision_score 
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
# code starts here 
model = LogisticRegression(random_state=6)
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
score = accuracy_score(y_test,y_pred)
print('Accuracy',score)
# Code ends here
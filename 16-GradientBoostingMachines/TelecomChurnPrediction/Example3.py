# AdaBoost Implementation
from Example2 import X_train,X_test,y_train,y_test
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

# Code starts here
print(X_train.head())
print(X_test.head())
print(y_train)
print(y_test)

ada_model = AdaBoostClassifier(random_state=0)
ada_model.fit(X_train,y_train)
y_pred = ada_model.predict(X_test)
ada_score = accuracy_score(y_test,y_pred)
ada_cm = confusion_matrix(y_test,y_pred)
ada_cr = classification_report(y_test,y_pred)

print(ada_score)
print(ada_cm)
print(ada_cr)
# Logistic Regression model
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score, confusion_matrix
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import roc_auc_score
import zipfile
path = 'Test.zip'
path = zipfile.ZipFile(path)
path = path.open('creditcard_new.csv')

# Code starts here
data = pd.read_csv(path)
X = data.drop(['Class'],axis=1)
y = data['Class']
# 'Stratified split' ensures that the proportion of majority class:minority class is same in both the test dataset and train dataset
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,stratify=y,random_state=0)
model = LogisticRegression(random_state=0)
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
accuracy = model.score(X_test,y_test)
recall = recall_score(y_test,y_pred)
precision = precision_score(y_test,y_pred)
f1 = f1_score(y_test,y_pred)
confusion_mat = confusion_matrix(y_test,y_pred)

print('Accuarcy',accuracy)
print('Recall',recall)
print('Precision',precision)
print('F1 Score',f1)
print('CF',confusion_mat)
# Code ends here
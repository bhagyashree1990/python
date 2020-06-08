# Adaboost Implementation
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier

#Loading of the data
path = 'Test.csv'
data = pd.read_csv(path)

#Extracting the features
X = data.drop(['deposit'],1)
#Extracting the target class
y = data['deposit'].copy()
#Splitting the dataset into test and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

#Fitting of Weak Classifier
dt_clf=DecisionTreeClassifier(max_depth=1,random_state=0)
dt_clf.fit(X_train,y_train)
dt_score = dt_clf.score(X_test,y_test)
print(dt_score)
# Fitting of weak classifier with Adaboost

ada_clf = AdaBoostClassifier(base_estimator=dt_clf,random_state=0)
ada_clf.fit(X_train,y_train)
ada_score = ada_clf.score(X_test,y_test)
print(ada_score)
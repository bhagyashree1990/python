# Naive Aggregation : Soft voting vs Hard voting
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier

#Different models initialised
log_clf_1 = LogisticRegression(random_state=0)
log_clf_2 = LogisticRegression(random_state=42)
decision_clf1 = DecisionTreeClassifier(criterion = 'entropy',random_state=0)
decision_clf2 = DecisionTreeClassifier(criterion = 'entropy', random_state=42)

#Creation of list of models
Model_List=[('Logistic Regression 1', log_clf_1),
            ('Logistic Regression 2', log_clf_2),
            ('Decision Tree 1', decision_clf1),
            ('Decision Tree 2', decision_clf2)]

# Code starts here
path='Test.csv'
data = pd.read_csv(path)
print(data.head(10))
#Features
X= data.drop(['deposit'],1)
#Target variable
y=data['deposit'].copy()
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0)
voting_clf_hard = VotingClassifier(estimators=Model_List,voting='hard')
voting_clf_hard.fit(X_train,y_train)
hard_voting_score = voting_clf_hard.score(X_test,y_test)

voting_clf_soft = VotingClassifier(estimators=Model_List,voting='soft')
voting_clf_soft.fit(X_train,y_train)
soft_voting_score = voting_clf_soft.score(X_test,y_test)

print(hard_voting_score)
print(soft_voting_score)
# Code ends here
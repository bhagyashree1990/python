# Using Stacking
from mlxtend.classifier import StackingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from Example1 import X_train,X_test,y_train,y_test
classifier1 = DecisionTreeClassifier(random_state=0)
classifier2 = DecisionTreeClassifier(random_state=1)
classifier3 = DecisionTreeClassifier(random_state=2)
classifier4 = DecisionTreeClassifier(random_state=3)
classifier_list=[classifier1,classifier2,classifier3,classifier4]
m_classifier=LogisticRegression(random_state=0)
# Code starts here
sclf = StackingClassifier(classifiers=classifier_list,meta_classifier=m_classifier)
sclf.fit(X_train,y_train)
s_score  = sclf.score(X_test,y_test)
print(s_score)
# Code ends here
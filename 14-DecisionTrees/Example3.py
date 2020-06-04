# Interpreting decision tree built in sklearn
# Getting the accuracy of test data using decision tree
from Example2 import data_train,data_test,label_train,label_test,tree
# Code starts here
dt2 = tree.DecisionTreeClassifier(max_depth=3)
dt2.fit(data_train,label_train)
dt2_score_train = dt2.score(data_train,label_train)
dt2_score_test = dt2.score(data_test,label_test)
print(dt2_score_train)
print(dt2_score_test)
# Code ends here
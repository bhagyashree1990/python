# Indicators of overfitting
# Observe overfitting of decision tree on data
# Reduce overfitting by max_depth
from Example2 import data_train,data_test,label_train,label_test,tree
#  Code starts here
dt4 = tree.DecisionTreeClassifier(criterion='entropy',max_depth=4,random_state=6)
dt4.fit(data_train,label_train)
dt4_score_train = dt4.score(data_train,label_train)
dt4_score_test = dt4.score(data_test,label_test)
print(dt4_score_train)
print(dt4_score_test)
dt_full = tree.DecisionTreeClassifier(criterion='entropy',random_state=6)
dt_full.fit(data_train,label_train)
dt_full_score_train = dt_full.score(data_train,label_train)
dt_full_score_test = dt_full.score(data_test,label_test)
print(dt_full_score_train)
print(dt_full_score_test)
# Code ends here
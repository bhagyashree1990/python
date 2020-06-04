# Pruning the tree
# Reduce overfitting by limiting the number of samples of leaf
from Example2 import data_train,data_test,label_train,label_test,tree
# Code starts here
dt_msl = tree.DecisionTreeClassifier(criterion='entropy',min_samples_leaf=100)
dt_msl.fit(data_train,label_train)
dt_msl_score_train = dt_msl.score(data_train,label_train)
dt_msl_score_test = dt_msl.score(data_test,label_test)
print(dt_msl_score_train)
print(dt_msl_score_test)
# Code ends here
#Decision tree visualization through sklearn
from Example1 import bank_full,bank_full_labels
# import packages

import numpy as np
import matplotlib.pyplot as plt
from io import StringIO
from sklearn.tree import export_graphviz
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn import metrics
from IPython.display import Image
import pydotplus


# Code starts here
data_train,data_test,label_train,label_test = train_test_split(bank_full,bank_full_labels,test_size=0.2, random_state=6)

dt2 = tree.DecisionTreeClassifier(max_depth=2,criterion='gini')
dt2.fit(data_train,label_train)

dot_data = tree.export_graphviz(dt2,out_file=None,feature_names=bank_full.columns, filled = True, class_names=['term_deposit_yes','term_deposit_no'])

graph_big = pydotplus.graph_from_dot_data(dot_data)

# show graph - do not delete/modify the code below this line
img_path = 'file.png'
graph_big.write_png(img_path)

plt.figure(figsize=(14,18))
plt.imshow(plt.imread(img_path))
plt.axis('off')
plt.show() 
# Code ends here
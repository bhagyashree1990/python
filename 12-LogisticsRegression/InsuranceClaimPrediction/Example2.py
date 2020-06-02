#Outlier Detection
import matplotlib.pyplot as plt
from Example1 import X_train,y_train
# Code starts here
X_train.boxplot(column='bmi')
q_value = X_train.bmi.quantile(q=0.95)
print(y_train.value_counts())
# Code ends here
# Target variable distribution
#Importing header files
import matplotlib.pyplot as plt
from Example1 import y_train
# Code starts here
fully_paid = y_train.value_counts()
plt.bar(fully_paid.index,fully_paid)
plt.show()
# Code ends here
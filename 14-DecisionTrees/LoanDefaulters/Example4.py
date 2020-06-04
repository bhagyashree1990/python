# Numerical Features Visualisation
from Example3 import num_df
from Example1 import y_train
#Importing header files
import seaborn as sns
import matplotlib.pyplot as plt
# Code starts here
cols = num_df.columns
fig, axes = plt.subplots(9,1, figsize=(20,10))
for i in range(0,9):
    sns.boxplot(x=y_train,y=num_df[cols[i]],ax=axes[i])
# Code ends here
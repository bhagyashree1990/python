#Predictor check!
import seaborn as sns
import matplotlib.pyplot as plt
from Example1 import X_train,y_train
# Code starts here
cols = ['children','sex','region','smoker']
fig, axes = plt.subplots(2,2, figsize=(20,10))
for i in range(0,2):
    for j in range(0,2):
        col = cols[i*2+j]
        sns.countplot(x=X_train[col],hue=y_train,ax=axes[i,j])
# Code ends here
#Categorical Features Visualisation
from Example3 import cat_df
from Example1 import y_train
#Importing header files
import seaborn as sns
import matplotlib.pyplot as plt
# Code starts here
cols = cat_df.columns
fig, axes = plt.subplots(2,2, figsize=(20,10))
for i in range(0,2):
    for j in range(0,2):
        sns.countplot(x=cat_df[cols[i*2+j]],hue=y_train,ax=axes[i,j])

# Code ends here
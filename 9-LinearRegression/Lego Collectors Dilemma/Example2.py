#Predictor Check!
import matplotlib.pyplot as plt
from Example1 import X_train, y_train
# code starts here        
cols = X_train.columns
fig, axes = plt.subplots(3,3, figsize=(20,10))
for i in range(0,3): #access row
    for j in range(0,3): #access col
        col = cols[i*3+j]
        axes[i,j].scatter(X_train[col],y_train)
        axes[i,j].set_xlabel(col)
        axes[i,j].set_ylabel('list_price')
# code ends here

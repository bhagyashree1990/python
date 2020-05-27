#Prediction Using Cross Validation
from sklearn.model_selection import cross_val_score
from Example1 import X_train, X_test, y_train, y_test,np
from sklearn.linear_model import LinearRegression
#Code starts here
regressor = LinearRegression()
score = cross_val_score(regressor,X_train,y_train,cv=10)
mean_score = np.mean(score)
print(mean_score)
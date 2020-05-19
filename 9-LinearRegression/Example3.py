# import packages
from sklearn.linear_model import LinearRegression 
from Example1 import X_train,y_train,np,X_test
# Code starts here
# instantiate linear model
linreg = LinearRegression()

# fit model on training data
linreg.fit(X_train, np.log(y_train))

# predict on test features
y_pred = linreg.predict(X_test)

# display predictions
print(y_pred)

# Code ends here
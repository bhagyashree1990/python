#Observe Underfitting
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from Example1 import X_train,X_test,y_train,y_test,np

# instantiate new model
# train and test sets with 100 features
new_X_train = X_train.iloc[:,:100]
new_X_test = X_test.iloc[:,:100]


# fit and predict
model_2 = LinearRegression()
model_2.fit(new_X_train,y_train)
pred_2 = model_2.predict(new_X_test)

# calculate RMSE
rsme_2 = np.sqrt(mean_squared_error(y_test,pred_2))
print(rsme_2)
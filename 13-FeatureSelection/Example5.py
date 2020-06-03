#Embedded Methods : LASSO/RIDGE
from Example1 import X,y,r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge

# Code starts here
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
lasso = Lasso(random_state=0)
lasso.fit(X_train,y_train)
y_pred_lasso = lasso.predict(X_test)
lasso_score = r2_score(y_test,y_pred_lasso)

ridge = Ridge(random_state=0)
ridge.fit(X_train,y_train)
y_pred_ridge = ridge.predict(X_test)
ridge_score = r2_score(y_test,y_pred_ridge)

print(lasso_score)
print(ridge_score)
# Code ends here
#Prediction Using Polynomial Regressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from Example1 import X_train, X_test, y_train, y_test
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
#Code starts here
model = make_pipeline(PolynomialFeatures(2), LinearRegression())
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
r2_poly = r2_score(y_test,y_pred)
print(r2_poly)
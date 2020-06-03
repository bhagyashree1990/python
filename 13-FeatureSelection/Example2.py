# Feature selection using Chi Squared Test
# import packages
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectKBest
from Example1 import ames,LinearRegression,r2_score,train_test_split
# Code starts here
X = ames.loc[:,ames.columns != 'SalePrice']
y = ames['SalePrice']
test = SelectKBest(score_func=chi2,k=60)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
X_train = test.fit_transform(X_train,y_train)
X_test = test.transform(X_test)
model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
chi2_score = r2_score(y_test,y_pred)
print(chi2_score)
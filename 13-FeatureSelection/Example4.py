# Feature Extraction with RFE
from pandas import read_csv
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import ExtraTreesClassifier
from Example1 import ames,train_test_split,r2_score
#no of features list
nof_list=[20,30,40,50,60,70,80]
#Variable to store the highest score
high_score=0
#Variable to store the optimum features
nof=0
#Code begins here
X = ames.loc[:,ames.columns != 'SalePrice']
y = ames['SalePrice']
for n in nof_list:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    model = LinearRegression()
    rfe = RFE(estimator=model,n_features_to_select=n)
    X_train_rfe = rfe.fit_transform(X_train,y_train)
    X_test_rfe = rfe.transform(X_test)
    model.fit(X_train_rfe,y_train)
    y_pred = model.predict(X_test_rfe)
    r2 = r2_score(y_test,y_pred)
    if high_score < r2:
        high_score = r2
        nof = n
print(high_score)
print(nof)
#Feature selection using correlation
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
path='Test.csv'
# Code starts here
ames = pd.read_csv(path)
#print(ames.columns)
X = ames.loc[:,ames.columns != 'SalePrice']
y = ames['SalePrice']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
X_train['Class'] = y_train
t_corr = X_train.corr()
t_corr = t_corr.loc[:,'Class']
#print(t_corr)
corr_columns = t_corr[abs(t_corr)>0.5]
corr_columns = corr_columns.drop('Class')
#print(corr_columns.index)
X_train_new = X_train.loc[:,corr_columns.index]
X_test_new = X_test.loc[:,corr_columns.index]
model = LinearRegression()
model.fit(X_train_new,y_train)
y_pred_new = model.predict(X_test_new)
corr_score = r2_score(y_test,y_pred_new)
print(corr_score)
# Code ends here
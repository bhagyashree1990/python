#Data Loading and Splitting
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# path- variable storing file path
path = 'test.csv'
#Code starts here
df = pd.read_csv(path)
print(df[df.columns[0:5]])

X = df.loc[:,df.columns != 'Price']
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=6)

corr = X_train.corr()
print(corr)
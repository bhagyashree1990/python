#Data loading and splitting
import pandas as pd
import sklearn.model_selection as model_selection
path='Test.csv'
df = pd.read_csv(path)
print(df.head())
X = df.loc[:,df.columns != 'list_price']
y = df['list_price']

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.3, random_state=6)
#Split into training and test datasets
# import packages
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
path = 'Test.csv'
# Code starts here
df = pd.read_csv(path)
X = df.iloc[:,0:7]
y = df.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)
print(X_train)
print(X_test)
# code ends here
#Data loading and splitting
# import the libraries
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

# Code starts here
path='Test.csv'
df = pd.read_csv(path)
print(df.iloc[:,0:5])
X = df.iloc[:,0:7]
y = df.iloc[:,-1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=6)

# Code ends here
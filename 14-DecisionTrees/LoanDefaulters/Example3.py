#Feature Split
#Importing header files
import numpy as np
from sklearn.preprocessing import LabelEncoder
from Example1 import X_train,X_test

# Code starts here
X_train['int.rate'] = X_train['int.rate'].map(lambda x: str(x)[:-1])
X_test['int.rate'] = X_test['int.rate'].map(lambda x: str(x)[:-1])
X_train['int.rate'] = X_train['int.rate'].astype(float)/100
X_test['int.rate'] = X_test['int.rate'].astype(float)/100
num_df = X_train.select_dtypes(include =['number']).copy()
cat_df = X_train.select_dtypes(include =['object']).copy()
print(num_df.columns)
print(cat_df.columns)
# Code ends here
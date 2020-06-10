# Data loading and cleaning
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Code starts here
path = 'Test.csv'
df = pd.read_csv(path)
print(df[df.columns[0:5]])
print(df.info)
df['INCOME'] = df['INCOME'].str.replace(r'\D', '')
df['HOME_VAL'] = df['HOME_VAL'].str.replace(r'\D', '')
df['BLUEBOOK'] = df['BLUEBOOK'].str.replace(r'\D', '')
df['OLDCLAIM'] = df['OLDCLAIM'].str.replace(r'\D', '')
df['CLM_AMT'] = df['CLM_AMT'].str.replace(r'\D', '')

X = df.drop(['CLAIM_FLAG'],axis=1)
y = df['CLAIM_FLAG']
count = y.value_counts()
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=6)

# Code ends here
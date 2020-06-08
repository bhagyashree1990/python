# Load data
import pandas as pd
from sklearn.model_selection import train_test_split
#path - Path of file 
path = 'Test.csv'
# Code starts here
df = pd.read_csv(path)
# print(df.columns)
#Extracting the features
X = df.drop(['customerID','Churn'],1)
#Extracting the target class
y = df['Churn']
#Splitting the dataset into test and train
X_train,X_test,y_train,y_test = train_test_split(X, y,test_size=0.3,random_state=0)

#Data Cleaning , Data preparation ...getting towards feature selection
#Import libraries 
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from Example1 import dataset
# Identify the unnecessary columns and remove it 
dataset.drop(columns=['Soil_Type7', 'Soil_Type15'], inplace=True)
# Scales are not the same for all variables. Hence, rescaling and standardization may be necessary for some algorithm to be applied on it.

X = dataset.iloc[:,:-1]
Y = dataset.iloc[:,-1]
r,c = dataset.shape
X_train,X_test,Y_train,Y_test =  train_test_split(X,Y,test_size=0.2,random_state=0)

#Standardized
#Apply transform only for continuous data
scaler = StandardScaler()
X_train_temp = scaler.fit_transform(X_train.iloc[:,:10])
X_test_temp = scaler.transform(X_test.iloc[:,:10])

#Concatenate scaled continuous data and categorical
X_train1 = np.concatenate((X_train_temp,X_train.iloc[:,10:c-1]),axis=1)
X_test1 = np.concatenate((X_test_temp,X_test.iloc[:,10:c-1]),axis=1)

scaled_features_train_df = pd.DataFrame(X_train1,index=X_train.index,columns=X_train.columns)
scaled_features_test_df = pd.DataFrame(X_test1,index=X_test.index,columns=X_test.columns)



import pandas as pd
filepath = 'Pokemon2.csv'
#Load the Pokemon dataset
df = pd.read_csv(filepath)
print(df)

#Quick Exploration of Data
print("------------------")
#1 Looking at the top few rows
print(df.head(5))
print("------------------")
#2 Looking at the last few rows:
print(df.tail(5))
#3 General information of every column
print("------------------")
print(df.info())
#4 Data type of every column: 
print("------------------")
print(df.dtypes)
#5 Check column names:
print("------------------")
print(df.columns)
#6 Check dimensions :
print("------------------")
print(df.shape)
#7 Check missing values per column
print("------------------")
print(df.isnull().sum())
#8 Check number of unique values per column
print("------------------")
print(df.nunique())
#9 Dropping missing values
print("------------------")
print(df.dropna())

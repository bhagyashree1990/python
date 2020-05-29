#Data Loading
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
path='Test.csv'
#Code starts here
#Exploration
data = pd.read_csv(path)
sns.distplot(data['Rating'].dropna())
#Cleaning
data = data[data['Rating']<=5]
sns.distplot(data['Rating'])
#Code ends here
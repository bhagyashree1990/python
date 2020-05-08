#HRM DataSet 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
path='HRData.csv'
df = pd.read_csv(path)
#Dataset columns
print(df.columns.values)
#Dataset rows and columns size
print(df.shape)

#Data Visualization

#PIE
dept = df['Department'].value_counts()
print(dept)
plt.figure(1)
plt.pie(dept,labels=dept.index,autopct='%1.1f%%')

#BAR
df['GenderID'].replace({0:"Male",1:"Female"},inplace=True)
gender = df['GenderID'].value_counts()
print(gender)
plt.figure(2)
plt.bar(gender.index,gender)

#STACKED BAR
dept_and_gender = df.groupby(['Department','GenderID']).size().unstack()
dept_and_gender.plot(kind='bar',stacked=True)
plt.xlabel("Department")
plt.ylabel("Gender")
plt.xticks(rotation=45)

#LINES
df['DateofHire']=pd.to_datetime(df['DateofHire'],format='%m/%d/%Y')
df['DateofTermination']=pd.to_datetime(df['DateofTermination'],format='%m/%d/%y')
hiring = df['DateofHire'].dt.year.value_counts(dropna=False).rename_axis('Year').reset_index(name='Hiring')
termination = df['DateofTermination'].dt.year.value_counts(dropna=False).rename_axis('Year').reset_index(name='Termination')
combined_df = pd.merge(left=hiring,right=termination,left_on='Year',right_on='Year',how='outer').sort_values(by='Year')
print(combined_df)

combined_df.plot(x='Year',y=['Hiring','Termination'])
#SHOW
plt.show()

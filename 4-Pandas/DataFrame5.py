#Selection, Creation, and Deletion
import pandas as pd
filepath = 'Pokemon2.csv'
#Load the Pokemon dataset
df = pd.read_csv(filepath)
# select column 'Name' from dataframe
print(df['Name'])
# select columns 'Name', 'HP' and 'Attack'
print(df[['Name','HP','Attack']])
# create column 'Difference' using 'Attack' and 'Defence'
df['Difference']=df['Attack']-df['Defense']
print(df)
# delete column 'Difference' permanently
df.drop(['Difference'],inplace=True,axis=1)
print(df)
# Access rows
print('---------')
print(df.loc[0])
print(df.iloc[0])

# Access particular cell 2nd row 4th col 
print(df.iloc[1,3])


# Slicing 
print('---------')
print(df[1:3])
# Creation/Addition
print('---------')
df = df.append(pd.DataFrame([[80,'Bhagyashree','Grass','Poison',0,0,0]],columns=df.columns))
print(df)
#Deletion
df.drop(index=0,axis=0,inplace=True)
print('---------')
print(df)


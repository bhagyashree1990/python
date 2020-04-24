#import packages
import pandas as pd
# Create DataFrames : From dictionary
#data source
data = {'Name':['Rob','Bobby','John','Danny','Manny'], 'Age':[25,30,21,32,23]}

#construct dataframe
df = pd.DataFrame(data, index = ['R','B','J','D','M'])

#display
print(df)
# Create DataFrames : From list of dictionary
# data source
data = [{'Name':'Rob','Age':25},{'Name':'Bobby','Age':30},
        {'Name':'John','Age':21},{'Name':'Danny','Age':32},
        {'Name':'Manny','Age':23}]

#construct dataframe
df = pd.DataFrame(data, index=['R','B','J','D','M'])
print('--------')
print(df)
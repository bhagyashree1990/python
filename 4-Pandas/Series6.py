#It may happen that while combining series you arrive at another series which contains null values or NaNs
#you can replace them with any value you want with the help of .fillna() method of pandas
import pandas as pd
a = pd.Series([1,2,3,4],index=[0,1,2,3])
b = pd.Series([1,2,3,4],index=[0,1,3,4])
c = a + b
print(c)
c.fillna(0,inplace=True)
print(c)
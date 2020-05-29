#Genre vs Rating
from Example5 import data
#Code starts here
print(data['Genres'].unique())
new = data['Genres'].str.split(";",n=1,expand=True)
data['Genres'] = new[0]
gr_mean = data[['Genres','Rating']].groupby(['Genres'],as_index=False).mean()
print(gr_mean.describe())
gr_mean = gr_mean.sort_values(by='Rating')
print(gr_mean.iloc[0])
print(gr_mean.iloc[-1])
#Code ends here
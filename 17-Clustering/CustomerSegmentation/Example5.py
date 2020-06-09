# Which cluster orders the most `Champagne`?
from Example4 import clusters
from Example1 import offers, transactions,pd
# Code starts here
# merge 'clusters' and 'transactions'
data = pd.merge(clusters,transactions,on='Customer Last Name')
# merge `data` and `offers`
data = pd.merge(data,offers)
print(data.head())

# initialzie empty dictionary
champagne = {}

# iterate over every cluster
for i in range(0,5):
    # observation falls in that cluster
    new_df = data[data['cluster'] == i]    
    # sort cluster according to type of 'Varietal'
    counts = new_df['Varietal'].value_counts(ascending=False)
    # check if 'Champagne' is ordered mostly
    if counts.index[0] == 'Champagne':
        # add it to 'champagne'
        champagne[i]=counts[0]
# get cluster with maximum orders of 'Champagne' 
cluster_champagne = max(champagne,key = champagne.get)
# print out cluster number
print(cluster_champagne)

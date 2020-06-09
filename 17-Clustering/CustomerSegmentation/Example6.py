# Which cluster of customers favours discounts more on an average?
# Code starts here
from Example5 import data
# empty dictionary
discount = {}
# iterate over cluster numbers
for i in range(0,5):
    # dataframe for every cluster
    new_df = data[data['cluster'] == i]  
    # average discount for cluster
    counts = new_df['Discount (%)'].mean()
    # adding cluster number as key and average discount as value 
    discount[i]=counts
# cluster with maximum average discount
cluster_discount  = max(discount,key=discount.get)
print(cluster_discount)
# Code ends here
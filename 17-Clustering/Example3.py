# Elbow method to find optimal number of clusters
# import packages
from sklearn.cluster import KMeans
from Example1 import df
import matplotlib.pyplot as plt
# Code starts here
# Empty list for storing WCSS across all values of k
dist = []
# Iterate from 1-9
for i in range(1,10):
    # Initialize KMeans algorithm
    km = KMeans(n_clusters=i,init='k-means++', max_iter=300, n_init=10, random_state=0)
    # Fit on data
    km.fit(df)   
    # Append WCSS to list storing WCSS
    dist.append(km.inertia_)
# Initialize figure
plt.figure(figsize=(10,10))
# Line plot # clusters on X-axis and WCSS on Y-axis 
plt.plot(range(1,10),dist)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('wcss')
plt.show()

# Code ends here
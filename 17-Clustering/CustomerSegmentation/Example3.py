# Use Kmeans to cluster data
from Example2 import matrix
# import packages
from sklearn.cluster import KMeans

# Code starts here
# initialize KMeans object
cluster = KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init=10, random_state=0)

# create 'cluster' column
matrix['cluster'] = cluster.fit_predict(matrix[matrix.columns[1:]])

print(matrix.head())
# Code ends here
# K-Means
# import packages
from sklearn.cluster import KMeans
from Example1 import df
# Code starts here
# Here,
# n_clusters: Number of clusters (K)
# init: Choice of initialization of cluster centroids; 
# k-means++ is considered a smart way to initialization
# n_iter: Number of time the k-means algorithm will be run with different centroid seeds
# max_iter: Maximum number of iterations of the k-means algorithm for a single run

# Cluster centers

# Within cluster sum of squares
# Initialize K-means algorithm
km = KMeans(n_clusters=6,init='k-means++', max_iter=300, n_init=10, random_state=0)
km.fit(df)
# Cluster centers
centroids = km.cluster_centers_
print("Cluster centers are:", centroids)
print('='*20)
# within cluster sum of squares (WCSS)
wcss = km.inertia_
print("Within cluster sum of squares is:", wcss)
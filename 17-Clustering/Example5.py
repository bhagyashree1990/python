# Finding the optimum number of clusters
# import packages
from sklearn.cluster import AgglomerativeClustering
from Example1 import df
import matplotlib.pyplot as plt
# initialize Agglomerative clustering object with 3 clusters
cluster = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')  

# predict on dataset
cluster.fit_predict(df)

# scater plot
plt.figure(figsize=(10, 7))  
plt.scatter(df.iloc[:,0], df.iloc[:,1], c=cluster.labels_, cmap='rainbow')
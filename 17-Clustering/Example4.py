# Important parameters for Agglomerative clustering
# Generate dendrogram
from Example1 import df
import matplotlib.pyplot as plt
# import panckages
import scipy.cluster.hierarchy as sch

# Code starts here
# initialize figure and axes
fig, ax_1 = plt.subplots(figsize=(20,10))
# Linkage criteria
# Single 
# Complete 
# Average 
# Ward 

# dendrogram with "ward" linkage
dend = sch.dendrogram(sch.linkage(df, method='ward'), leaf_rotation=90, ax=ax_1)
# plot on a figure
ax_1.set_title("Dendrogram")
ax_1.set_xlabel('Customer')
ax_1.set_ylabel('euclidean')
plt.show()
# Code ends here
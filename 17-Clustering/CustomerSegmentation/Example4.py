# Visualize clusters using PCA
# import packages
from sklearn.decomposition import PCA
from Example3 import matrix
# Code starts here
# initialize pca object with 2 components
pca = PCA(n_components=2, random_state=0)
# create 'x' and 'y' columns donoting observation locations in decomposed form
matrix['x'] = pca.fit_transform(matrix[matrix.columns[1:]])[:,0]
matrix['y'] = pca.fit_transform(matrix[matrix.columns[1:]])[:,1]
# dataframe to visualize clusters by customer names
clusters = matrix.iloc[:,[0,33,34,35]]

# visualize clusters
clusters.plot.scatter(x='x',y='y',c='cluster',colormap='viridis')

# Code ends here
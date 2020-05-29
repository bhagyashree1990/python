#Solving with linear regression
# import packages
from Example1 import np, data
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
#%matplotlib inline

# instantiate model
linear_model = LinearRegression()
df = data
# fit the model
linear_model.fit(df[['entropy']], df[['class']])

# generate 1000 X-values
X_sample = np.linspace(-9, 3, 1000)

# calculate y-values for 1000 X-values
Y_sample = X_sample*linear_model.coef_[0] + linear_model.intercept_

# threshold for entropy
threshold  = (0.5 - linear_model.coef_[0]) / linear_model.intercept_
print(threshold)

# scatter plot 
plt.scatter(df[['entropy']], df[['class']], marker='x')

# axes specifications
plt.xlabel('Entropy')
plt.ylabel('Class {1:Authentic, 0:Fake}')
plt.ylim(-0.1, 1.1)

# threshold lines
plt.axvline(threshold, linestyle='--', color='green')
plt.axhline(0.5, linestyle='--', color='black')

# line plot
plt.plot(X_sample, Y_sample, color='red')

# display plot
plt.show()
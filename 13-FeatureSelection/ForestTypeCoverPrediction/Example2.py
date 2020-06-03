#Exploratory Data Analysis
# We will visualize all the attributes using Violin Plot - a combination of box and density plots
import seaborn as sns
from matplotlib import pyplot as plt
from Example1 import dataset
#names of all the attributes 
cols = dataset.columns
#number of attributes (exclude target)
size = len(cols)-1
#x-axis has target attribute to distinguish between classes
x = cols[size]
#y-axis shows values of an attribute
y = cols[0:size]
#Plot violin for all attributes
for i in range(0,size):
    sns.violinplot(data=dataset,x=x,y=y[i])
    plt.show()
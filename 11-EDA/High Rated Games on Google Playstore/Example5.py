#Price vs Ratings
from Example4 import data
import seaborn as sns
#Code starts here
print(data['Price'].value_counts())
data['Price'] = data['Price'].str.replace(r'\D','').astype(float)
sns.regplot(x="Price",y="Rating",data=data).set(title='Rating vs Price [RegPlot]')
#Code ends here
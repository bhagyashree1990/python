#Last Updated vs Rating
from Example5 import data
import pandas as pd
import seaborn as sns
#Code starts here
print(data['Last Updated'])
data['Last Updated'] = pd.to_datetime(data['Last Updated'],format='%B %d, %Y')
max_date = max(data['Last Updated'])
print(max_date)
data['Last Updated Days'] = (max_date - data['Last Updated']).dt.days
sns.regplot(x="Last Updated Days",y="Rating",data=data).set(title='Rating vs Last Updated [RegPlot]')
#Code ends here
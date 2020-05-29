#Installs vs Ratings
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from Example2 import data
import seaborn as sns

#Code starts here
print(data['Installs'].value_counts())
data['Installs'] = data['Installs'].str.replace(r'\D','').astype(int)
le = LabelEncoder()
data['Installs'] = le.fit_transform(data['Installs'])
sns.regplot(x="Installs",y="Rating",data=data).set(title='Rating vs Installs [RegPlot]')
#Code ends here
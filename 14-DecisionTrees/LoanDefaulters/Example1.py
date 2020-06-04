# Data loading
#Importing header files
import pandas as pd
from sklearn.model_selection import train_test_split

path = 'Test.csv'
# Code starts here
data = pd.read_csv(path)
X = data.drop(['customer.id','paid.back.loan'],axis=1)
y = data['paid.back.loan']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0)

# Code ends here
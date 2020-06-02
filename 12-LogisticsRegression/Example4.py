#Model building using scikit-learn: Preprocess data
# import packages
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from Example1 import data
# Code starts here
X_train, X_test, y_train, y_test = train_test_split(data.iloc[:,:4], data['class'], test_size=0.2, random_state=42)

scaler = MinMaxScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train,y_train)
y_pred  = model.predict(X_test)
# Code ends here
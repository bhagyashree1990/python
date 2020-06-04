#Model Building
#Importing header files
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from Example1 import X_train,y_train,X_test,y_test
from Example3 import cat_df
# Code starts here
for col in cat_df.columns:
    #Train
    X_train[col].fillna('NA',inplace=True)
    le = LabelEncoder()
    X_train[col] = le.fit_transform(X_train[col])
    #Test   
    X_test[col].fillna('NA',inplace=True)
    X_test[col] = le.fit_transform(X_test[col])
#Replace No with 0 and Yes with 1
y_train = y_train.replace(to_replace=['Yes','No'],value=['1','0'])
y_test = y_test.replace(to_replace=['Yes','No'],value=['1','0'])
model = DecisionTreeClassifier(random_state=0)
model.fit(X_train,y_train)
acc = model.score(X_test,y_test)
print(acc)
# Code ends here
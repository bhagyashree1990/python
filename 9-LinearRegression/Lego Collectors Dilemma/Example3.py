#Reduce feature redundancies!
from Example1 import X_train,X_test
# Code starts here
corr = X_train.corr()
print(corr)
# If two features are correlated and with a value greater than 0.75, remove one of them.
# drop columns from X_train
X_train.drop(['play_star_rating','val_star_rating'],axis = 1 ,inplace=True)

# drop columns from X_test
X_test.drop(['play_star_rating','val_star_rating'], axis = 1 ,inplace=True)

# Code ends here
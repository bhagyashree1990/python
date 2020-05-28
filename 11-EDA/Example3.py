#Treatment of outliers: Out LIARS!
from Example1 import X_train,X_test,y_train,pd
# Code starts here
train = pd.concat([X_train,y_train],axis=1)
mask1 = train['LotFrontage']<300
mask2 = train['TotalBsmtSF']<5000
mask3 = train['GrLivArea']<4500
mask4 = train['LotArea']<100000
train = train[mask1 & mask2 & mask3 & mask4]
# Code ends here
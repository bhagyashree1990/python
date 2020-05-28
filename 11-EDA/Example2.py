#Detect Outlier
# Import packages
import matplotlib.pyplot as plt
from Example1 import X_train, y_train
# Code starts here
fig, ((ax_1, ax_2), (ax_3, ax_4)) = plt.subplots(2,2)
ax_1.scatter(X_train['LotFrontage'],y_train,color='red')
ax_1.set_title('LotFrontage vs SalePrice')
ax_1.set_xlabel('LotFrontage')
ax_1.set_ylabel('SalePrice')
ax_2.scatter(X_train['TotalBsmtSF'],y_train,color='blue')
ax_2.set_title('TotalBsmtSF vs SalePrice')
ax_2.set_xlabel('TotalBsmtSF')
ax_2.set_ylabel('SalePrice')
ax_3.scatter(X_train['GrLivArea'],y_train,color='green')
ax_3.set_title('GrLivArea vs SalePrice')
ax_3.set_xlabel('GrLivArea')
ax_3.set_ylabel('SalePrice')
ax_4.scatter(X_train['LotArea'],y_train,color='black')
ax_4.set_title('LotArea vs SalePrice')
ax_4.set_xlabel('LotArea')
ax_4.set_ylabel('SalePrice')

plt.show()
# Code ends here 
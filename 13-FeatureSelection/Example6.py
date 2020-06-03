# PCA(Principal Component Analysis)
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA 
from Example1 import ames,LinearRegression,r2_score
# Code starts here
X = ames.loc[:,ames.columns != 'SalePrice']
y = ames['SalePrice']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
pca = PCA(n_components=35,random_state=0)
X_train_pca = pca.fit_transform(X_train_scaled)
X_test_pca = pca.transform(X_test_scaled)
model = LinearRegression()
model.fit(X_train_pca,y_train)
y_pred_pca = model.predict(X_test_pca)
pca_score = r2_score(y_test,y_pred_pca)
print(pca_score)

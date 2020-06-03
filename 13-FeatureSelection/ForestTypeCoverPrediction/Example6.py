#Effect of feature selection on model prediction
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score
from Example4 import X_train,Y_train,X_test,Y_test,scaled_features_train_df,scaled_features_test_df
from Example5 import top_k_predictors
clf = OneVsRestClassifier(LogisticRegression())
clf1 = OneVsRestClassifier(LogisticRegression())

model_fit_all_features = clf1.fit(X_train,Y_train)
predictions_all_features = clf1.predict(X_test)
score_all_features = accuracy_score(Y_test,predictions_all_features)

model_fit_top_features = clf.fit(scaled_features_train_df[top_k_predictors],Y_train)
predictions_top_features = clf.predict(scaled_features_test_df[top_k_predictors])
score_top_features = accuracy_score(Y_test,predictions_top_features)

print(score_all_features)
print(score_top_features)

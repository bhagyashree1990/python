#Feature Selection using Select percentile
from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import f_classif
from Example4 import X_train1,Y_train,scaled_features_train_df,pd
# Code starts here
skb = SelectPercentile(score_func=f_classif,percentile=90)
predictors = skb.fit_transform(X_train1,Y_train)
scores = list(skb.scores_)
Features = scaled_features_train_df.columns
dataframe = pd.DataFrame({'Features':Features,'Scores':scores})
dataframe = dataframe.sort_values(by='Scores',ascending=False)
top_k_predictors = list(dataframe['Features'][:predictors.shape[1]])
print(top_k_predictors)
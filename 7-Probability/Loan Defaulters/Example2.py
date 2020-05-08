#Bayes theorem
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
path='Test.csv'
df = pd.read_csv(path)
# code starts here
prob_lp = df[df['paid.back.loan'] == 'Yes'].shape[0]/df.shape[0]
prob_cs = df[df['credit.policy'] == 'Yes'].shape[0]/df.shape[0]
new_df = df[df['paid.back.loan'] == 'Yes']
prob_pd_cs = new_df[new_df['credit.policy'] == 'Yes'].shape[0]/new_df.shape[0]

bayes = prob_pd_cs * prob_lp / prob_cs
print(bayes)
# code ends here
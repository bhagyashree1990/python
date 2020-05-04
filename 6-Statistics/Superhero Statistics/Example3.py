#Combat Correlation
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = 'heroes_information.csv'
data = pd.read_csv(path)

#Code starts here
sc_df = data[['Strength','Combat']].copy()
sc_covariance = sc_df.cov().iloc[0,1]
sc_strength = sc_df.Strength.std()
sc_combat = sc_df.Combat.std()
sc_pearson = sc_covariance / (sc_strength * sc_combat)
print(sc_pearson)
ic_df = data[['Intelligence','Combat']].copy()
ic_covariance = ic_df.cov().iloc[0,1]
ic_intelligence = ic_df.Intelligence.std()
ic_combat = ic_df.Combat.std()
ic_pearson = ic_covariance / (ic_intelligence * ic_combat)
print(ic_pearson)
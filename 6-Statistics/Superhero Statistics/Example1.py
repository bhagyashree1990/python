#Data loading
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = 'heroes_information.csv'
#Code starts here 
data = pd.read_csv(path)
data['Gender'].replace('-','Agender',inplace=True)
gender_count = data['Gender'].value_counts()
plt.bar(gender_count.index,gender_count)

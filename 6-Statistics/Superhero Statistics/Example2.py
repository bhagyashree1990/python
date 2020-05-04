#Heroes Alignment
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = 'heroes_information.csv'
#Code starts here 
data = pd.read_csv(path)
alignment = data['Alignment'].value_counts()
plt.pie(alignment,labels=alignment.index)
plt.show()
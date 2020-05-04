#Overpowered Super Beings
#Header files
import pandas as pd
import matplotlib.pyplot as plt

path = 'heroes_information.csv'
data = pd.read_csv(path)

#Code starts here
total_high = data.Total.quantile(q=0.99)
super_best = data[data['Total'] > total_high]
super_best_names = super_best['Name'].tolist()
print(super_best_names)
#Box Plots
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
path='AmesHousing.csv'
df = pd.read_csv(path)
df.boxplot(column='SalePrice')
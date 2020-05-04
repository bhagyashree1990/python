#Inter - Quartile Range
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
path='AmesHousing.csv'
df = pd.read_csv(path)
q1 = df.SalePrice.quantile(q=0.25)
q3 = df.SalePrice.quantile(q=0.75)
iqr = q3-q1
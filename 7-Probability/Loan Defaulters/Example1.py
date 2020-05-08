#Independence check 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
path='Test.csv'
df = pd.read_csv(path)
p_a = df[df['fico'].astype(float) >700].shape[0]/df.shape[0]
p_b = df[df['purpose']=='debt_consolidation'].shape[0]/df.shape[0]
df1 = df[df['purpose']=='debt_consolidation']
p_a_b = df1[df1['fico'].astype(float)>700].shape[0]/df1.shape[0]
result = (p_a == p_a_b)
print(result)
# code ends here
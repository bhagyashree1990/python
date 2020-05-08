#Purpose vs paid back loan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
path='Test.csv'
df = pd.read_csv(path)
# code starts here
purpose = df['purpose'].value_counts()
plt.bar(purpose.index,purpose,color='b',label='Purpose')

df1 = df[df['paid.back.loan'] == 'No']
purpose_df1 = df1['purpose'].value_counts()
plt.bar(purpose_df1.index,purpose_df1,color='r',label='Paid Back Loan')
plt.xticks(rotation=45)
plt.show()
# code ends here
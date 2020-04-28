# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
path = "Data.csv" 
# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)

# code ends here
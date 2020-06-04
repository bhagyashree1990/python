# import packages
import pandas as pd
feature_path='Feature.csv'
label_path='Label.csv'
# Code starts here
bank_full = pd.read_csv(feature_path)
bank_full_labels = pd.read_csv(label_path)
print(bank_full.head())
# Code ends here
from Example2 import *
#Dropping columns
banks = bank.drop(['Loan_ID'],axis=1)
#To see the null values
print(banks.isnull().sum())
# apply mode
bank_mode = banks.mode().iloc[0]
# fill missing nodes
banks.fillna(bank_mode,inplace=True)
print(banks.isnull().sum())
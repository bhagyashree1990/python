from Example3 import *
loan_term = banks['Loan_Amount_Term'].apply(lambda x:int(x)/12)
big_loan_term = len(loan_term[loan_term>=25])
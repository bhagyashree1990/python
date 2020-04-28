from Example3 import *
avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount')
print(avg_loan_amount)
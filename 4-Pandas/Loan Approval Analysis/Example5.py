from Example3 import *
loan_approved_se = len(banks.query('Self_Employed == "Yes" & Loan_Status == "Y"'))
loan_approved_nse = len(banks.query('Self_Employed == "No" & Loan_Status == "Y"'))
Loan_Status  = 614
percentage_se = loan_approved_se * 100 / Loan_Status
percentage_nse = loan_approved_nse * 100 / Loan_Status
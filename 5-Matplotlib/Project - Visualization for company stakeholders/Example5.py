#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load data
path = 'Data.csv'
data = pd.read_csv(path)

#Code starts here
fig, (ax_1, ax_2, ax_3) = plt.subplots(3,1, figsize=(20,10))
# plot scatter plot between 'ApplicantIncome' and LoanAmount using ax_1
ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])
ax_1.set_title('Applicant Income')
# Plot scatter plot between 'CoapplicantIncome' and LoanAmount using ax_2
ax_2.scatter(data['CoapplicantIncome'],data["LoanAmount"])
ax_2.set_title('Coapplicant Income')
#Plot scatter plot between 'TotalIncome' and LoanAmount using ax_3
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']
ax_3.scatter(data['TotalIncome'],data["LoanAmount"])
ax_3.set_title('Total Income')

plt.show()
#Data Reading
# Importing header files
import numpy as np
path = 'Test.csv'
# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data = np.genfromtxt(path,delimiter=',',skip_header=1)

census = np.concatenate((data,new_record))
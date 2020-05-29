#Make your own sigmoid function
import numpy as np
# Code starts here
def sigmoid(x):
    return 1/(1+np.exp(-x))
result = sigmoid(0)
print(result)
# Code ends here
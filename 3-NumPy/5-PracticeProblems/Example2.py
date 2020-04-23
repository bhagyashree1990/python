#Convert from Centigrade to Fahrenheit
# Code starts here
import numpy as np
# centigrade temperatures
centigrade_temps = np.array([0, 10, 25, 32, 80, 99.99])

# function for conversion
def convert(celsius):
    F = 9*celsius/5 + 32
    return F

fahrenheit_temps = convert(centigrade_temps)
# display fahrehheit temperatures
print(fahrenheit_temps)

# Code ends here
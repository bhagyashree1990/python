x1, y1, x2, y2, d1, d2 = 5, 5, 'Hello', 'Hello',  {'a':1, 'b':2}, {'a':1, 'b':2}
# is
#Evaluates to true if the variables on either side of the operator point to the same object and false otherwise
# is not
#Evaluates to false if the variables on either side of the operator point to the same object and true otherwise

x1_is_y1 = x1 is y1
print(x1_is_y1)

x2_is_y2 = x2 is y2
print(x2_is_y2)

d1_is_d2 = d1 is d2
print(d1_is_d2)
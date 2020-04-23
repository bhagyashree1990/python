# import reduce
from functools import reduce

# function to divide two numbers
def add(x,y):
    return x + y

# reduce function
reduced = reduce(add, ['a', 'b', 'c'])
print(reduced)
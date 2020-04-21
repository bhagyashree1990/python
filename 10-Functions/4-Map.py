# function to square numbers
def square(x):
    return x**2
# map function
mapped = list(map(square, [1,2,3,4]))
print(mapped)
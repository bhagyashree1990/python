# function to check if number is positive
def positive(x):
    return x > 0

# filter function
filtered = list(filter(positive, [-3,-2,-1,1,2,3,]))
print(filtered)
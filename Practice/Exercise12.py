# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
# and makes a new list of only the first and last elements of the given list. 

def list_ends(num):
    result = []
    result.append(num[0])
    result.append(num[-1])
    return result

a = [5, 10, 15, 20, 25]
print(list_ends(a))
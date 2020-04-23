def even_addition(values):
    #List Comprehension
    evens = [i for i in values if not i%2]
    return sum(evens) 

print(even_addition([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
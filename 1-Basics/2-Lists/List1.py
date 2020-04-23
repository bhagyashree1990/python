# initial list
scores = [80,90,95,100]

# memory location of initial list
print('Memory loaction initially is ' , id(scores))
print('='*20)

# change value
scores[2] = 99
# display modified list
print(scores)
print('='*20)

# check memory loaction of modified list 
print('Memory location of modified list is ' , id(scores))
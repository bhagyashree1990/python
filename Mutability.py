#initial variable
a = 50
# initial memory location
print(id(a))
#modified variable
a += 1
# new memory location, is it same?
print(id(a))

# intial list 
l = [1,2,3,4]
# initial memory location
print(id(l))
print('='*20)
# new list
l.append(5)
print(l)
print('='*20)
# new memory location
print(id(l))
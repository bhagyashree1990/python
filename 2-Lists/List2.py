a = [1,2,3]
b = [4,5,6]
num = [10,20,30]
#Len
print(len(a))
#Concatenation
c = a+b
print(c)
#Repitition
c = a*2
d = a*3
print(c)
#Membership
print(3 in a)
#Returns item from the list with max value
print(max(a))
#Returns item from the list with min value
print(min(a))
#Adds 10 to the end of the list
a.append(10)
print(a)
#Appends the contents of b to a
a.extend(b)
print(a)
#Returns the lowest index in the list that 1 appears in
print(d.index(1))
#Reverses objects of list in place
b.reverse()
print(b)
#Removes and returns last object from list
x = b.pop()
print(x)
print(b)
#Removes object 2 from list
d.remove(2)
print(d)
#Sum
total = sum(num)
print(total)
#Mean
mean = total /len(num)
print(mean)
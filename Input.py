print("Enter name:")
name= input()
print("Welcome "+name)
if False:
    m , n  = input().split()
    m , n  = int(m) , int(n)
    my_array = []
    for i in range(int(m)):
        row = [ int(x) for x in input().split()]
        my_array.append(row)
    print(my_array)
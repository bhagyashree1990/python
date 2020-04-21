myFile = open('Test.txt','r')
lines = myFile.readlines()
for i in lines:
    print(i)
myFile.close()
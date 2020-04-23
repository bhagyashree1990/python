name = 'Hello World!'
try:
    char = name[15]
    print(char)
except IndexError:
    print('IndexError has been found!')
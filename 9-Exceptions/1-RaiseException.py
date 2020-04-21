# custom input
num = int(input())

# raise exception if input is negative
if num < 0:
    raise Exception('{} is negative, please enter a positive number'.format(num))

# print input number if it is not negative
print('Your number is accepted!')
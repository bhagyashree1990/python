s = 'qA2'
contains_aplhanum = False
contains_alpha = False
contains_digit = False
contains_lower = False
contains_upper = False
for a in s:
    if a.isalnum():
        contains_aplhanum = True
    if a.isalpha():
        contains_alpha = True
    if a.isdigit():
        contains_digit = True
    if a.islower():
        contains_lower = True
    if a.isupper():
        contains_upper = True    
print(contains_aplhanum)        
print(contains_alpha)
print(contains_digit)
print(contains_lower)
print(contains_upper)
def count_substring(string, sub_string):
    count = 0 
    j = 0   
    for i in range(len(string)):
        index = string.find(sub_string,j)        
        if index >= 0:
            count += 1
            i = index+1
            j = index+1
    return count

string = 'ininini' #input().strip()
sub_string = 'ini' #input().strip()

count = count_substring(string, sub_string)
print(count)
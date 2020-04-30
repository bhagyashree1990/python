def reverse_words_order_and_swap_cases(sentence):
    list1 = []
    for word in sentence.split(' '): 
        str1 = ''
        for i in word:            
            if i.islower():
                result = i.upper()
            elif i.isupper():
                result = i.lower()
            else:
                result = i    
            str1 += result                    
        list1.append(str1)
    return ' '.join(list1[::-1]) 


print(reverse_words_order_and_swap_cases("aWESOME is cODING"))
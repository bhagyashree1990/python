# File path for message 6
file_path_6 = 'Num6.txt'
from Example2 import *
###
message_6 = read_file(file_path_6)
print(message_6)

even_word = lambda x : (len(x) % 2 == 0)

def extract_msg(message_f):
    a_list = message_f.split()
    b_list = list(filter(even_word,a_list))
    final_msg = ' '.join(b_list)
    return final_msg

secret_msg_4 = extract_msg(message_6)    
# File path for message 4  and message 5
file_path_4 = 'Num4.txt'
file_path_5 = 'Num5.txt'
from Example2 import *
#Code starts here
message_4 = read_file(file_path_4)
message_5 = read_file(file_path_5)
print(message_4)
print(message_5)

def compare_msg(message_d,message_e):
    a_list = message_d.split()
    b_list = message_e.split()
    c_list = [x for x in a_list if x not in b_list]
    final_msg = ' '.join(c_list)
    return final_msg

secret_msg_3 = compare_msg(message_4,message_5)
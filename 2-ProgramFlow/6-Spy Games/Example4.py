file_path_3 = 'Num3.txt'
from Example2 import *
###
message_3 = read_file(file_path_3)

def substitute_msg(message_c):
    sub = None
    if message_c == 'Red':
        sub = 'Army General'
    elif message_c == 'Green':
        sub = 'Data Scientist'
    elif message_c == 'Blue':
        sub = 'Marine Biologist'
    return sub

secret_msg_2 = substitute_msg(message_3)
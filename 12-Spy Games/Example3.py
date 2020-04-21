file_path_1 = 'Num1.txt'
file_path_2 = 'Num2.txt'
from Example2 import *
### 
message_1 = read_file(file_path_1)
message_2 = read_file(file_path_2)

def fuse_msg(message_a,message_b):
    quotient = int(message_b)//int(message_a)
    return quotient

secret_msg_1 = str(fuse_msg(message_1,message_2))
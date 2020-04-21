from Example3 import *
from Example4 import *
from Example5 import *
from Example6 import *
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]
final_path= '/secret_message.txt'

#Code starts here
secret_msg = ' '.join(message_parts)

def write_file(secret_msg,path):
    file = open(path,'a+')
    file.write(secret_msg)
    file.close()

write_file(secret_msg,final_path)
print(secret_msg)
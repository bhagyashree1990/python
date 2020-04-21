##File path for the file 
file_path = 'Test.txt'
    
#Code starts here
def read_file(path):
    file = open(path,'r')
    sentence = file.readline()
    file.close()
    return sentence

sample_message = read_file(file_path)
from os import strerror

try:
    stream = open("text.txt")
    lines = stream.readlines()
    for line in lines:
        print("1 : ", line)
    stream.close()
    
except IOError as e:
    print("I/O error occured:", strerror(e.errno))

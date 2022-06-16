from os import strerror
data = bytearray(10)
try:
    bf = open("myfile.bin", 'wb')
    bf.write(data)
    bf.close()

except IOError as e:
    print("I/O error occured:", strerror(e.errno))
    

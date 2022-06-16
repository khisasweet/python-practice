from os import strerror
data = bytearray(10)
try:
    bf = open("myfile.bin", 'wb')
    bf.write(data)
    bf.close()

except IOError as e:
    print("I/O error occured:", strerror(e.errno))
    
try:
    bf = open('myfile.bin','rb')
    data = bytearray(bf.red())
    bf.close()
    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occured:", strerror(e.errno))        

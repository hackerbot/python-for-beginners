buffersize = 100000
input = open('bigfile.txt','r')
output = open('newbigfile.txt', 'w')
buffer = input.read(buffersize)
bufferlimit = 1000000

while len(buffer):
    output.write(buffer)
    print('.', end='')
    buffer = input.read(buffersize)
    
#file = open('ch10lab.txt')

#for line in file:
#    print(line, end = '')
    
#while len(buffer):
#    output.write(buffer)
#    print('.', end='')
#    buffer = input.read(buffersize)
    

class LogMessage:
#    buffersize = 1000000
#    buffer = input.read(buffersize)
#    bufferlimit = 1000000
    def __init__(self,filename):
        self.filename = filename
        print(filename, 'has been initialized and opened.')
    def read(self):
        for line in open(self.filename, 'r'):
            return print(line, end = '')
    def write(self):
        data = input("What would you like to add the the file?\n")
        self.read.append(data)
        self.write = open('new'+self.filename, 'w')
        for line in open(self.write, 'r'):
            return print(line,'new'+self.filename, end = '')

file1 = LogMessage('ch10lab.txt')
print(file1.filename)
print(file1.read())
print(file1.write())

#initialize filename
#
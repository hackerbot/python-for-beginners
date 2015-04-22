#buffersize = 100000
#input = open('bigfile.txt','r')
#output = open('newbigfile.txt', 'w')
#buffer = input.read(buffersize)
#bufferlimit = 1000000

#while len(buffer):
#    output.write(buffer)
#    print('.', end='')
#    buffer = input.read(buffersize)
    

class LogMessage:
    def __init__(self,filename):
        self.filename = filename
        print(filename, 'has been successfully initialized.')
    def read(self): #read and print
        for line in open(self.filename, 'r'):
            print(line, end = '')
        return ''
    def write(self): #write
        data = input("What would you like to add to the file?\n")
        self.filenamenew = 'new'+self.filename
        buffersize = 100000
        original = open(self.filename, 'r')
        output = open(self.filenamenew, 'w')
        buffer = original.read(buffersize) #def buffer
        bufferlimit = 1000000
        while len(buffer): #while buffering
            output.write(buffer)
            print(buffer, end='')
            output.write('\n'+data) #writes out input to a new line in the file
            break #no infinite loop
        print('\nInputed data has been added to the new file', self.filenamenew)
        return '' #to clear none message

file1 = LogMessage('ch10lab.txt')
file2 = LogMessage('newch10lab.txt')
print(file1.filename)
print(file1.read())
print(file1.write())
#checking work
print(file2.filename)
print(file2.read())
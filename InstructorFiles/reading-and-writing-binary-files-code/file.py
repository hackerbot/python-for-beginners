buffersize = 100000
input = open('keyboard_bokeh.jpg','rb')
output = open('image2.jpg', 'wb')
buffer = input.read(buffersize)

while len(buffer):
    output.write(buffer)
    print('.', end='')
    buffer = input.read(buffersize)
    
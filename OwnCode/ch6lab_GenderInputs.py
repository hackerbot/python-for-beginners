data = input('Enter the first initial of your gender:\n')
if data == 'm' or data == 'M':
    print('You have entered "{}" that means you are a male!'.format(data))
elif data == 'f' or data == 'F':
    print('You have entered "{}" that means you are a female!'.format(data))
else:
    while data != 'm' or data != 'M' or data != 'f' or data != 'F':
        data = input('You have entered: "{}".\nPlease enter a valid initial of your gender:\n'.format(data))
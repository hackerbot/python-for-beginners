def datatyper():
    'Takes input and tells you what it is also returns same type of output.'
    boolean = True or False
    integer = int(1)
    data = input("Enter a string that you want to classify it's data type:\n")
    if type(data) == type(boolean):
        return boolean(data)
        print('You have entered "{}" and this is a boolean.'.format(data))
    elif type(data) == type(integer):
        print('You have entered "{}" and this is an integer.'.format(data))
        return integer(data)
    else:
        print('You have entered "{}" and this is an alphanumeric.'.format(data))
        return data

datatyper()

boolean = True or False
integer = int(1)
#data = int(boolean(input("Enter a string that you want to classify it's data type:\n")))
if type(data) == type(boolean):
    print('You have entered "{}" and this is a boolean.'.format(data))
elif type(data) == type(integer):
    print('You have entered "{}" and this is an integer.'.format(data))
else:
    print('You have entered "{}" and this is an alphanumeric.'.format(data))
    
print(type(data))
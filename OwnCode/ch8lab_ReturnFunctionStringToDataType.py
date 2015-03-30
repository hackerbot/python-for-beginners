def datatyper():
    'Takes input and tells you what it is also returns same type of output.'
    boolean = 'false' or 'true' or False or True
    integer = int(1)
    print("Enter a string that you want to classify it's data type:")
    data = input()
    type(data) == type(input())
    if type(input) == type(boolean):
        return boolean(data)
        print('You have entered "{}" and this is a boolean.'.format(data))
    elif type(input) == type(integer):
        print('You have entered "{}" and this is an integer.'.format(data))
        return integer(data)
    else:
        print('You have entered "{}" and this is an alphanumeric.'.format(data))
        return data

datatyper()

#boolean = True or False
#integer = int(1)
#data = int(boolean(input("Enter a string that you want to classify it's data type:\n")))
#if data = int(input("Enter a string that you want to classify it's data type:\n")):
#    return print(type(data))
#if type(data) == type(boolean):
#    print('You have entered "{}" and this is a boolean.'.format(data))
#elif type(data) == type(integer):
#    print('You have entered "{}" and this is an integer.'.format(data))
#else:
#    print('You have entered "{}" and this is an alphanumeric.'.format(data))    
#print(type(data))
def datatyper():
    'Takes input and returns same type of input as an output.'
    boolean = ('false' or 'true' or 'False' or 'True')
    integer = (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 0)
    data = input("Enter data into function that returns similar data:\n")
    if data == boolean:
        return boolean
        print('You have entered "{}" and this is a boolean.'.format(data))
    elif data == integer:
        return integer
        print('You have entered "{}" and this is a digit.'.format(data))
    elif data != (boolean or integer):
        return data
        print('You have entered "{}" and this is an alphanumeric.'.format(data))
    else:
        return 'Input Error'
print(datatyper())

#def datatyper():
#    'Takes input and tells you what it is also returns same type of output.'
#    boolean = 'false' or 'true' or False or True
#    integer = int(1)
#    print("Enter a string that you want to classify it's data type:")
#    data = input()
#    if type(input) == type(boolean):
#        return 'You have entered "{}" and this is a boolean.'.format(data)
#    elif type(input) == type(integer):
#        return 'You have entered "{}" and this is an integer.'.format(data)
#    elif type(input) != (type(boolean) or type(integer)):
#        return 'You have entered "{}" and this is an alphanumeric.'.format(data)
#    else:
#        return 'Input Error'
#print(datatyper())
def datatyper():
    'Takes input and returns what type of input it was'
    data = input("Enter data into function that returns similar data:\n")
    if data == True or data == False or data == 'false' or data == 'true':
        return 'You have entered "{}" and this is a boolean.'.format(data)
    elif data.isdigit():
        return 'You have entered "{}" and this is a digit.'.format(data)
    elif data.isalnum():
        return 'You have entered "{}" and this is an alphanumeric.'.format(data)
    else:
        return 'Input Error'
print(datatyper())
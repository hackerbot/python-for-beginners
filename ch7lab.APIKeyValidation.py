string = '82914656273523:a4edFea2786DGex'
print('API Key Verification:')
print(string)
# sequence = string.split(':')
# print(sequence)

id = string[0:14]
key = string[16:]
# print(id)
# print(key)

# counting numbers 0-9 in ID
numbercount = id.count('1') + id.count('2') + id.count('3') + id.count('4') + id.count('5') + id.count('6') + id.count('7') + id.count('8') + id.count('9') + id.count('0')

# ID verification
if numbercount == 14 and len(id) == 14:
    print("ID valid with {} numbers.".format(numbercount))
    if 20 > len(key) > 10:
        print("Key is also valid with {} characters.".format(len(key)))
        print('All is good!')
    else:
        print('...but Key is not valid becauase it has {} characters.'.format(len(key)))
else:
    print("ID error.")


# Checking individual counts
# print(id.count('0'))
# print(id.count('1'))
# print(id.count('2'))
# print(id.count('3'))
# print(id.count('4'))
# print(id.count('5'))
# print(id.count('6'))
# print(id.count('7'))
# print(id.count('8'))
# print(id.count('9'))


print('AND:')
print('A B Q')
x,y = 1,2 #comparing values
a,b = 2,1 #input values
if a >= x and b < y: print('1 1 1')
elif a < x and b >= y: print('0 0 0')
elif a >= x and b >= y: print('1 0 0')
elif a < x and b < y: print ('0 1 0')
else: print('invalid input')

print('OR:')
print('A B Q')
x,y = 1,2 #comparing values
a,b = 2,1 #input values
if a >= x or b >= y: print('1 1 1')
elif a < x or b < y: print('0 0 0')
elif a >= x or b < y: print('1 0 1')
elif a < x or b > y: print('0 1 0')
else: print('invalid input')

print('NOT:')
x = 1 #comparing values
a = 2 #input values
var = 'Q = 0' if not a >= x else 'Q = 1'
print(var)

print('CHALLENGE:')
print('A B C Q')
x,y,z = 3,2,1
a,b,c = 1,2,3
if a >= x and b >= y or c >= z: print('1 1 1 1')
if a >= x and b < y or c >= z: print('1 0 1 1')
if a >= x and b <= y or c < z: print ('1 1 0 1')
if a >= x and b < y or c < z: print('1 0 0 0')
if a < x and b >= y or c < z: print('0 1 0 0')
if a < x and b < y and c >= z: print('0 0 1 1')
if a < x and b < y and c < z: print ('0 0 0 0')
if a < x and b >= y and c >= z: print('0 1 1 1')
else: print('invalid input')
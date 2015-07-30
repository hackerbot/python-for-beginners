print ('orv1')
print('A B Q')

a,b,q = 10,20,30
var = '1 1 1' if a >= 1 or b >= 20 or q >= 30 else 'default'
print(var)

a,b,q = 1,2,3
var = '1 1 1' if a >= 1 or b >= 20 or q >= 30 else 'default'
print(var)

a,b,q = 1,2,3
var = '1 1 1' if a >= 1 or b >= 20 or q >= 30 else 'default'
print(var)

print ('AND')
print('A B Q')

a,b,q = 3,2,1 # firstrow
if a >= b and b >= q and q < a: print('1 1 1')
elif a >= b and b >= q and q >= a: print('1 1 0')
elif a < b and b >= q and q < a: print('0 1 1')
elif a >= b and b < q and q < a: print('1 0 1')
elif a >= b and b < q and q >= a: print('1 0 0')
elif a < b and b >= q and q >= a: print('0 1 0')
elif a < b and b < q and q < a: print('0 0 1')
elif a < b and b < q and q >= a: print('0 0 0')
else: print('default')

a,b,q = 1,2,3 # secondrow
if a >= b and b >= q and q < a: print('1 1 1')
elif a >= b and b >= q and q >= a: print('1 1 0')
elif a < b and b >= q and q < a: print('0 1 1')
elif a >= b and b < q and q < a: print('1 0 1')
elif a >= b and b < q and q >= a: print('1 0 0')
elif a < b and b >= q and q >= a: print('0 1 0')
elif a < b and b < q and q < a: print('0 0 1')
elif a < b and b < q and q >= a: print('0 0 0')
else: print('default')
    
a,b,q = 2,1,3 # thirdrow
if a >= b and b >= q and q < a: print('1 1 1')
elif a >= b and b >= q and q >= a: print('1 1 0')
elif a < b and b >= q and q < a: print('0 1 1')
elif a >= b and b < q and q < a: print('1 0 1')
elif a >= b and b < q and q >= a: print('1 0 0')
elif a < b and b >= q and q >= a: print('0 1 0')
elif a < b and b < q and q < a: print('0 0 1')
elif a < b and b < q and q >= a: print('0 0 0')
else: print('default')

a,b,q = 1,2,2 # fourthrow
if a >= b and b >= q and q < a: print('1 1 1')
elif a >= b and b >= q and q >= a: print('1 1 0')
elif a < b and b >= q and q < a: print('0 1 1')
elif a >= b and b < q and q < a: print('1 0 1')
elif a >= b and b < q and q >= a: print('1 0 0')
elif a < b and b >= q and q >= a: print('0 1 0')
elif a < b and b < q and q < a: print('0 0 1')
elif a < b and b < q and q >= a: print('0 0 0')
else: print('default')

print ('OR')
print('A B Q')

a,b,q = 3,2,1 # firstrow
if a >= 10 or b >= 20 or q < 30: print('1 1 1')
elif a >= b or b >= q or q >= a: print('1 1 0')
elif a < b or b >= q or q < a: print('0 1 1')
elif a >= b or b < q or q < a: print('1 0 1')
elif a >= b or b < q or q >= a: print('1 0 0')
elif a < b or b >= q or q >= a: print('0 1 0')
elif a < b or b < q or q < a: print('0 0 1')
elif a < b or b < q or q >= a: print('0 0 0')
else: print('default')

a,b,q = 1,2,3 # secondrow
if a >= b or b >= q or q < a: print('1 1 1')
elif a >= b or b >= q or q >= a: print('1 1 0')
elif a < b or b >= q or q < a: print('0 1 1')
elif a >= b or b < q or q < a: print('1 0 1')
elif a >= b or b < q or q >= a: print('1 0 0')
elif a < b or b >= q or q >= a: print('0 1 0')
elif a < b or b < q or q < a: print('0 0 1')
elif a < b or b < q or q >= a: print('0 0 0')
else: print('default')
    
a,b,q = 2,1,3 # thirdrow
if a >= b or b >= q or q < a: print('1 1 1')
elif a >= b or b >= q or q >= a: print('1 1 0')
elif a < b or b >= q or q < a: print('0 1 1')
elif a >= b or b < q or q < a: print('1 0 1')
elif a >= b or b < q or q >= a: print('1 0 0')
elif a < b or b >= q or q >= a: print('0 1 0')
elif a < b or b < q or q < a: print('0 0 1')
elif a < b or b < q or q >= a: print('0 0 0')
else: print('default')

a,b,q = 1,2,2 # fourthrow
if a >= b or b >= q or q < a: print('1 1 1')
elif a >= b or b >= q or q >= a: print('1 1 0')
elif a < b or b >= q or q < a: print('0 1 1')
elif a >= b or b < q or q < a: print('1 0 1')
elif a >= b or b < q or q >= a: print('1 0 0')
elif a < b or b >= q or q >= a: print('0 1 0')
elif a < b or b < q or q < a: print('0 0 1')
elif a < b or b < q or q >= a: print('0 0 0')
else: print('default')

if a == 'true' or b == 'true': print('true')
elif a == 'false' or b == 'false': print('false')
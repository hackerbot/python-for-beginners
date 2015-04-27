print('Fibonacci Sequence')
#inputs
f0 = 0
f1 = 1
x = False
#sequence loop
while True:
    fn = f0 + f1
    f0 = f1
    f1 = fn
    if (fn > 100):
        x = True
    else:
        x = False
    print(fn)
    if (x == True):
        break

#correct numbers for verification
0
1
2
3
5
8
13
21
34
55
89
144
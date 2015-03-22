print('Fibonacci Sequence')
#inputs
a = 0
b = 1
c = 2
d = 3
e = 5
f = 8
g = 13

#sequence
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
#sequence loop
while g < 200:
    print(g)
    g += f
    f += e
    e += d
    d += c
    c += b
    b += a
else:
    print('sequence >= 100')
    
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
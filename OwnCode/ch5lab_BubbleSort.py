print('Bubble Sort')
list = [8,7,12,4,9,6,5]
print(list)

list2 = sorted(list) #list2 = list sorted
print(list2) #correct answer regular sort

l = len(list) #length of list
print(l)

b = 0
a = 0
while l > a and l > b:
    a += 1
    print(list[a - 2:a]) #print of pre-bubble cache
    if list[a - 2] < list[a - 1] or list[a - 2] == list[a - 1]:
        continue
    elif list[a - 2] > list[a - 1] and a < l:
        list2 = sorted(list[a - 2:a])
        print(list2) #print of bubble cache
        del list[a - 2:a]
        list.insert(a - 2,list2[0])
        list.insert(a - 1,list2[1])
        print(list)
        if a == l + 1:
            a = 0
            b += 1
    else: print('Bubble Sorted')
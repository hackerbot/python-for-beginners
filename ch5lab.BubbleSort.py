print('Bubble Sort')
list = [8,7,12,4,9,6,5]
print(list)

list3 = sorted(list) # list2 = list sorted

l = len(list) # length of list

a = 0
while l >= a:
    a += 1
    if list[a - 1] >= list[a - 2]:
        continue
    elif list[a - 2] > list[a - 1]:
        list2 = sorted(list[a - 2:a])
        del list[a - 2:a]
        list.insert(a - 2,list2[0])
        list.insert(a - 1,list2[1])
        a = 1
        if list == sorted(list3):
            print(list)
            print('Bubble Sorted')
            break
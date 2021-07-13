def lab36(*l):
    size = len(l)
    c = l[0]
    for i in range(1,size):
        c = list(set(c) & set(l[i]))
    if len(c) == 0:
        return "True"
    else:
        return "False"

list1 = ['a', 'b', 2]
list2 = ['a', 3, 'b', 3]
list3 = ['a', 3, 'd', 2]
print(lab36(list1, list2, list3))

def lab34(a, b):
    if b < a:
        a, b = b, a
    new_list = ()
    max = 0
    for i in range(a, b + 1):
        s = 0
        for j in range(i, 0, -1):
            if i % j == 0:
                s += 1
        if max < s:
            max = s
    for i in range(a, b + 1):
        s = 0
        for j in range(i, 0, -1):
            if i % j == 0:
                s += 1
        if s == max:
            new_list = new_list + (i,)
    return new_list

print("Введите два числа через пробел: ")
a, b = map(int, input().split())
print(lab34(a, b))

def lab35(list):
    size = len(list)
    count = 0
    for i in range(size-1):
        for j in range(i+1,size):
            if str(list[i]) == str(list[j]):
                count += 1
    if count > 0:
        return "False"
    else:
        return "True"

print("Введите данные через пробел: ")
lst = input().split()
print(lab35(lst))

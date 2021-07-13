def lab33(n):
    if n > 0:
        start = [1]
        print(start)
    if n > 1:
        start = [1, 1]
        print(start)
    for i in range(2, n):
        line = [1] + list(map(lambda x: x[0] + x[1], zip(start, start[1:]))) + [1]
        print(line)
        start = line

print("Введите количество строк: ")
n = int(input())
lab33(n)

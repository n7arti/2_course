import random
from threading import Thread


def sum(mas, begin, step, N):
    summa = 0
    for i in range(begin, step):
        summa += mas[i] ** (1 + i / N)


def with_threading(mas, begin, step, N):
    T1 = Thread(target=sum, args=(mas, begin, step))
    T1.start()
    T1.join()


if __name__ == '__main__':
    Z = 0
    T = int(input("Введите количество потоков: "))
    while True:
        N = int(input("Введите количество элементов в массиве Х, кратное 4: "))
        if (N % 4 != 0):
            print("Некоректный ввод, попробуйте снова!")
        else:
            break

    X = [0.0] * N
    for i in range(N):
        X[i] = random.random()
        print(X[i])

    if (N % T == 0):
        K = N / T
    else:
        K = N // T
    for i in range(T):
        with_threading(X, Z, K, N)
        Z += K

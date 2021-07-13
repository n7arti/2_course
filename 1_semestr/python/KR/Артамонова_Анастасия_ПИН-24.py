import random
from threading import Thread


def sum(mas, begin, step, N, summa):
    for i in range(begin, step):
        summa += mas[i] ** (1 + i / N)
    if (begin + step + 1 == N):
        print("Значение: ", summa)


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

    if (N % T == 0):
        K = int(N / T)
    else:
        K = int(N / T)
    summa = 0
    for i in range(T):
        T1 = Thread(target=sum, args=(X, Z, K, N, summa,))
        T1.start()
        T1.join()
        Z += K

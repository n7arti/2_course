from threading import Thread
import random
from time import time


def without_threading():
    P1 = [i for i in range(1, 5001)]
    Q1 = [i for i in range(1, 5001)]
    R1 = [[i * 0.0] * 5000 for i in range(5000)]
    for i in range(len(R1)):
        for j in range(len(R1[i])):
            R1[i][j] = 1 / (1 + abs(Q1[j] - P1[i]))


def vector(mas):
    for i in range(5000):
        mas[i] = random.randint(0, 10)


def matrix(mas1, mas2):
    mas3 = [[i * 0.0] * 5000 for i in range(5000)]
    for i in range(5000):
        for j in range(5000):
            mas3[i][j] = 1 / (1 + abs(mas2[j] - mas1[i]))


def with_threading():
    P2 = [i for i in range(5000)]
    Q2 = [i for i in range(5000)]
    t1 = Thread(target=vector, args=(P2,))
    t2 = Thread(target=vector, args=(Q2,))
    t3 = Thread(target=matrix, args=(P2, Q2,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()


if __name__ == '__main__':
    start = time()
    without_threading()
    print("Time without threading", time() - start)
    start = time()
    with_threading()
    print("Time with threading", time() - start)

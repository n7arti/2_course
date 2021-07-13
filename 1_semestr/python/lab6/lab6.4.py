import os
from threading import Thread
from time import time


def find(key, file):
    if (file.endswith(".txt")) and (key in file):
        return 1


def withone(key):
    path = os.path.dirname(__file__)
    for address, dirs, files in os.walk(path):
        for file in files:
            process = Thread(target=find, args=(key, file,))
            if (process.start() == 1):
                print(address + "/" + file)
                process.join()


def findtxt(file):
    if file.endswith(".txt"):
        return 1


def findkey(file, key):
    if key in file:
        return 1


def withtwo(key):
    path = os.path.dirname(__file__)
    for address, dirs, files in os.walk(path):
        for file in files:
            process1 = Thread(target=findtxt, args=(file,))
            process2 = Thread(target=findkey, args=(file, key,))
            if (process1.start() == 1) and (process2.start() == 1):
                print(address + "/" + file)
                process2.join()
                process1.join()



if __name__ == '__main__':
    key = input("Введите ключевое слово: ")
    start = time()
    withone(key)
    print("Один поток: ", time() - start)
    start = time()
    withtwo(key)
    print("Два потока: ", time() - start)

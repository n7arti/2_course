import threading

semaphore = threading.BoundedSemaphore()
semaphore.acquire()  # уменьшает счетчик (-1)
semaphore.release()  # увеличивает счетчик (+1)


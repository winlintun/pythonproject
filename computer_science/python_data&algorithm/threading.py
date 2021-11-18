from threading import *

counter = 0
lock = RLock()

#sem = Semaphore(2)
def increment():
    global counter

    for i in range(0, 2000):
        #sem.acquire()
        lock.acquire()
        counter += 1
        lock.release()


def decrement():
    global counter
    for i in range(0, 2000):
        lock.acquire()
        counter -= 1
        lock.release()

thread1 = Thread(target=increment)
thread2 = Thread(target=decrement)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Counter: ", counter)
import threading
from threading import *
import time
"""

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

"""


print("Main Thread Start.")

def chil_task(x):
    print(x, "Chil thread start.")
    time.sleep(1)
    print(x, "Chil therad end.")
    #time.sleep(1)





thread1 = threading.Thread(target=chil_task, args=(1,))
thread1.start()

thread2 = threading.Thread(target=chil_task, args=(2,))
thread2.start()

thread1.join()
thread2.join()


#thread.join()

#time.sleep(1)
print("Main Thread End.")

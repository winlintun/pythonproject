from threading import *

"""
class MyThread(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self) -> None:
        for i in range(1, 50):
            print("Thread: ", self.name, 'i', i)

ThreadA = MyThread('ThreadA')

ThreadB = MyThread("ThreadB")

ThreadA.start()
ThreadB.start()

"""


counter = 0

def increment():
    global counter
    for i in range(0, 2000000):
        counter += 1


def decrement():
    global counter
    for i in range(0, 2000000):
        counter -= 1

thread1 = Thread(target=increment)
thread2 = Thread(target=decrement)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Counter: ", counter)



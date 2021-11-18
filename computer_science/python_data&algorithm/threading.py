import threading
from threading import *
import time



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
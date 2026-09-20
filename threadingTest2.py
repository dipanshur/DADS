import threading
import time

def worker(name):
    print(f"{name} Starting")
    time.sleep(2)
    print(f"{name} Finished")


# worker("thread1")
# worker("thread2")

t1 = threading.Thread(target=worker, args=("Thread-1", ))
t2 = threading.Thread(target=worker, args=("Thread-2", ))

t1.start()
t2.start()

#Join() --> wait for the thread to finish

t1.join()
t2.join()
import threading
import time

def task():
    for i in range(3):
        print("Task Running")
        time.sleep(1)

t1 = threading.Thread(target=task)
t1.start()
t1.join()
# task()
print("Main thread is Running")
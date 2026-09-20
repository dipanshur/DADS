from multiprocessing import Process
import threading
import time

def task():
    for i in range(3):
        print("Task Running")
        time.sleep(2)


if __name__ == "__main__":

    # t = threading.Thread(target=task)
    # t.start()

    p = Process(target=task)
    p.start()

    print("Main Process Running")

    p.join()
import queue
import time
import threading

def putElem():
    while True:
        q.put(time.time())
        time.sleep(5)

def getElem():
    while True:
        try:
            # elem = q.get(block=False)
            # elem = q.get(timeout=2)
            elem = q.get_nowait()
            print("get:{0}".format(elem))
        except queue.Empty:
            print("queue is empty!")
        time.sleep(1)


if __name__ == "__main__":
    q = queue.Queue()

    thread1 = threading.Thread(target=putElem)
    thread1.start()

    thread2 = threading.Thread(target=getElem)
    thread2.start()

    thread1.join()
    thread2.join()
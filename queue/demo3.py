import queue
import threading
import time

def getElem():
    while True:
        elem = q.get()
        print("get:{}".format(elem))
        q.task_done()
        time.sleep(1)

if __name__ == '__main__':
    q = queue.Queue(maxsize=10)
    [q.put(i) for i in range(1, 11)]
    threading.Thread(target=getElem, daemon=True).start()

    q.join()
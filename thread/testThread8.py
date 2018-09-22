import threading
import time

count = 0

def adder(addLock):
    global count
    with addLock:
        count += 1
    time.sleep(0.5)
    with addLock:
        count += 1

addLock = threading.Lock()
threads = []

for i in range(100):
    thread = threading.Thread(target=adder, args=(addLock,))
    thread.start()
    threads.append(thread)

[thread.join() for thread in threads]

print count

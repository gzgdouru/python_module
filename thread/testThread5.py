import thread
import time

lock = thread.allocate_lock()
numThreads = 5
mutexList = [thread.allocate_lock() for i in range(numThreads)]

def counter(myId, count, mutex):
    for i in range(count):
        time.sleep(1 / (myId + 1))
        with mutex:
            print "[%s] => %s" % (myId, i)

    mutexList[myId].acquire()

for i in range(numThreads):
    thread.start_new_thread(counter, (i, 5, lock))

while not all(mutex.locked() for mutex in mutexList):
    time.sleep(0.25)

print "main thread existing..."
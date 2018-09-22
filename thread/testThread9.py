import thread
import time
import Queue
import threading

totalConsumers = 2
totalProducers = 4
totalMessage = 4

safeprint = thread.allocate_lock()
dataQueue = Queue.Queue()

def producer(idnum):
    for msgNum in range(totalMessage):
        time.sleep(idnum)
        dataQueue.put("[producer id=%d, count=%d]" % (idnum, msgNum))

def consumer(idNum):
    while True:
        time.sleep(0.1)
        try:
            data = dataQueue.get(block=False)
        except Queue.Empty:
            pass
        else:
            with safeprint:
                print "consumer",idNum, "got=>", data

if __name__ == "__main__":
    '''
    for i in range(totalConsumers):
        thread.start_new_thread(consumer, (i,))

    for i in range(totalProducers):
        thread.start_new_thread(producer, (i,))

    time.sleep((totalProducers -1) * totalMessage + 1)
    print "Main thread exit..."
    '''

    for i in range(totalConsumers):
        tmpThread = threading.Thread(target=consumer, args=(i,))
        tmpThread.daemon = True
        tmpThread.start()

    waitFor = []
    for i in range(totalProducers):
        tmpThread = threading.Thread(target=producer, args=(i, ))
        waitFor.append(tmpThread)
        tmpThread.start()

    for tmpThread in waitFor:
        tmpThread.join()

    print "Main thread exit..."
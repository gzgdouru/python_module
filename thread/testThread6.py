import threading

class MyThread(threading.Thread):
    def __init__(self, myId, count, mutex):
        self.myId = myId
        self.count = count
        self.mutex = mutex
        threading.Thread.__init__(self)

    def run(self):
        for i in range(self.count):
            with self.mutex:
                print "[%s] => %s" % (self.myId, i)


lock = threading.Lock()
threads = []

for i in range(10):
    thread = MyThread(i, 100, lock)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print "main thread existing..."
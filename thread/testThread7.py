import thread
import threading

def action(i):
    print i ** 32

class MyThread(threading.Thread):
    def __init__(self, num):
        self.i = num
        threading.Thread.__init__(self)

    def run(self):
        print self.i ** 32


#MyThread(2).start()

#tmpThread = threading.Thread(target=(lambda : action(2)))
#tmpThread.start()

#threading.Thread(target=action, args=(2,)).start()

thread.start_new_thread(action, (2,))



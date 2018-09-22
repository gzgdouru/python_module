import thread

lock = thread.allocate_lock()
#mutexList = [thread.allocate_lock() for i in range(10)]
flag = [False] *10

def counter(myId, count):
    for i in range(count):
        lock.acquire()
        print "[%s] => %s" % (myId, i)
        lock.release()

    #mutexList[myId].acquire()
    flag[myId] = True

for j in range(10):
    thread.start_new_thread(counter, (j, 100))

'''
for mutex in mutexList:
    while not mutex.locked():
        pass
'''

while False in flag:
    pass

print "main thread exiting..."

import thread
import time

def child(tid):
    print "hello from thread", tid

def parent():
    i = 1
    while True:
        i += 1
        thread.start_new_thread(child, (i,))
        if raw_input() == "q": break

parent()
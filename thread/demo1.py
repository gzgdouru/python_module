import threading
import time

def printInfo():
    thread = threading.current_thread()
    while True:
        print("{}:我有一直小菜鸡!".format(thread.getName()))
        time.sleep(2)

if __name__ == "__main__":
    thread1 = threading.Thread(target=printInfo, args=())
    thread1.setDaemon(True)
    thread1.start()

    thread2 = threading.Thread(target=printInfo, args=())
    # thread2.setDaemon(True)
    thread2.start()

    time.sleep(3)
    print("base thread ok!")


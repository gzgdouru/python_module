import threading, time
import random


def light():
    if not even.is_set():
        even.set()
    count = 0
    while True:
        if count < 10:
            print("---green light on---")
        elif count < 13:
            print("---yellow light on---")
        elif count < 20:
            if even.is_set():
                even.clear()
            print("---red light on---")
        else:
            count = 0
            even.set()

        time.sleep(1)
        count += 1


def car(n):
    while True:
        time.sleep(random.randrange(3))
        if even.isSet():  # 如果是绿灯
            print("car [%s] is running.." % n)
        else:
            print("car [%s] is waiting for the red light.." % n)


if __name__ == "__main__":
    even = threading.Event()
    Light = threading.Thread(target=light)
    Light.start()

    for i in range(3):
        t = threading.Thread(target=car, args=(i,))
        t.start()

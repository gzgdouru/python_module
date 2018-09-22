import threading, time


class Gov(threading.Thread):
    def __init__(self, cond):
        super(Gov, self).__init__()
        self.cond = cond

    def run(self):
        global num
        # self.cond.acquire()
        with self.cond:
            while True:
                print("开始拉升股市")
                num += 1
                print("拉升了{0}个点".format(num))
                time.sleep(2)
                if num == 5:
                    print("暂时安全")
                    self.cond.notify()
                    self.cond.wait()
                    # self.cond.release()


class Consumers(threading.Thread):
    def __init__(self, cond):
        super(Consumers, self).__init__()
        self.cond = cond

    def run(self):
        global num
        # self.cond.acquire()
        with self.cond:
            while True:
                if num > 0:
                    print("开始打压股市")
                    num -= 1
                    print("打压了{0}个点".format(num))
                    time.sleep(2)
                elif num == 0:
                    print("你妹的！天台在哪里")
                    self.cond.notify()
                    self.cond.wait()
                    # self.cond.release()


if __name__ == "__main__":
    cond = threading.Condition()
    num = 0

    c = Consumers(cond)
    c.start()

    time.sleep(1)

    p = Gov(cond)
    p.start()

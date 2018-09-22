import time

if __name__ == "__main__":
    print("time.localtime:")
    print(time.localtime().tm_year)
    print(time.localtime(1304575584.1361799))
    print("-"*100)

    print("time.gmtime:")
    print(time.gmtime())
    print("-"*100)

    print("time.time:")
    print(time.time())
    print("-"*100)

    print("time.mktime:")
    print(time.mktime(time.localtime()))
    print("-"*100)

    print("time.sleep:")
    time.sleep(2)
    print(time.localtime())
    print("-"*100)

    print("time.clock:")
    time.sleep(1)
    print(time.clock())
    time.sleep(1)
    print(time.clock())
    time.sleep(1)
    print(time.clock())
    print("-"*100)

    print("time.asctime:")
    print(time.asctime())
    print(time.asctime(time.localtime()))
    print("-"*100)

    print("time.ctime:")
    print(time.ctime())
    print(time.ctime(time.time()))
    print("-"*100)

    print("time.strftime:")
    print(time.strftime("%Y-%m-%d %X"))
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print("-" * 100)

    print("time.strptime:")
    print(time.strptime("2018-06-01 12:00:00", "%Y-%m-%d %H:%M:%S"))
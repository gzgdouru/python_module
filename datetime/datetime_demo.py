from datetime import datetime
import time

if __name__ == "__main__":
    a = datetime.now()
    print(a)
    print(a.date())
    print(a.time())
    print(a.utctimetuple())
    print(a.timetuple())
    print(datetime.utcnow())
    print(datetime.utcfromtimestamp(time.time()))
    print(datetime.fromtimestamp(time.time()))
    print(time.time(), datetime.now().timestamp())
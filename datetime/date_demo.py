from datetime import date
import time

if __name__ == "__main__":
    a = date.today()
    print(a.year, a.month, a.day)
    print("-" * 10)

    a = date(2017, 3, 1)
    b = date(2017, 3, 17)
    print(a > b)
    print((b - a).days)
    print("-" * 100)

    a = date.today()
    print(a.isocalendar())
    print(a.isoformat())
    print(a.isoweekday())
    print(a.weekday())
    print("-" * 100)

    a = date.today()
    print(a.timetuple())
    print(a.toordinal())
    print(a.ctime())
    print(date.fromtimestamp(time.time()))
    print("-" * 100)


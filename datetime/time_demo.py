from datetime import time as dtime

if __name__ == "__main__":
    a = dtime(12, 20, 59, 899)
    print(a)
    print(a.hour, a.minute, a.second, a.microsecond)
    print("-" * 100)
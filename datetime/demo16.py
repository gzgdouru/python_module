import time
from datetime import datetime
from datetime import timedelta

def getDiffDays(strFirstDate, strSecondDate):
    fDate = datetime.strptime(strFirstDate, "%Y-%m-%d")
    sDate = datetime.strptime(strSecondDate, "%d/%m/%Y")
    return (sDate - fDate).days

def getDays(strDate):
    date = datetime.strptime(strDate, "%Y-%m-%d")
    return (datetime.now() - date).days

def diffDays(strDate):
    days = 0
    now = datetime.now()
    strDate = str(now.year) + "-" + strDate
    date = datetime.strptime(strDate, "%Y-%m-%d")
    if now <= date:
        days = (date - now).days
    else:
        date = datetime(year=date.year + 1, month=date.month, day=date.day)
        days = (date - now).days

    return days

if __name__ == "__main__":
    firstDate = "2017-08-15"
    secondDate = "30/11/2017"
    print(getDiffDays(firstDate, secondDate))

    print(getDays("1992-08-15"))
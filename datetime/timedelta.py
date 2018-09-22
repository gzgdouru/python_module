from datetime import datetime, timedelta, date

# 获取上一个月的最后一天
def get_last_month_last_day(today):
    first_date = date(today.year, today.month, 1)
    last_month = first_date - timedelta(days=1)
    return last_month.day

# 获取上个星期一和上个星期天的日期
def get_last_monday_and_last_sunday(today):
    today_weekday = today.isoweekday()
    last_sunday = today - timedelta(days=today_weekday)
    last_monday = last_sunday - timedelta(days=6)
    return last_monday, last_sunday

#获取当月的最后一天
def get_last_day(today):
    next_month_first_day = date(today.year+1, 1, 1) if today.month == 12 else date(today.year, today.month+1, 1)
    return (next_month_first_day - timedelta(days=1)).day

if __name__ == "__main__":
    now = datetime.now()
    print(get_last_day(now.date()))
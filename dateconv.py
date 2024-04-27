import datetime
import time
import pytz


def checkdate(timeinfo) -> bool:
    for t in timeinfo:
        if t.count(':') != 0:
            time = list(map(str, t.split(':')))
        else:
            date = list(map(str, t.split('.')))

    if len(date) == 3:
        year = int(date[2])
    else:
        year = datetime.datetime.now(pytz.timezone('Europe/Moscow')).year
    try:
        month = int(date[1])
        day = int(date[0])

        hour = int(time[0])
        minute = int(time[1])

    except:
        return False

    if len(time) != 2: return False

    try:
        newDate = datetime.datetime(year, month, day, hour, minute)
        correct_date = True
    except:
        correct_date = False
        return correct_date
    if datetime.datetime(year, month, day, hour, minute) - datetime.datetime.now() >= datetime.timedelta(
            0) and correct_date:
        is_future = True
    else:
        is_future = False

    return is_future and correct_date


def to_unix(timeinfo) -> float:
    for t in timeinfo:
        if t.count(':') != 0:
            time = t.split(':')
        else:
            date = t.split('.')

    if len(date) == 3:
        year = int(date[2])
    else:
        year = datetime.date.today().year
    month = int(date[1])
    day = int(date[0])

    hour = int(time[0])
    minute = int(time[1])

    dt = datetime.datetime(year, month, day, hour, minute)
    return (dt - datetime.datetime(1970, 1, 1)).total_seconds()


def from_unix(unixtime: int):
    return datetime.datetime.fromtimestamp(unixtime)

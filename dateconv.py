import datetime
import time
import pytz

logs = open('logs.txt', 'w')

now = datetime.datetime.now(pytz.timezone("Europe/Moscow"))

def checkdate(timeinfo) -> bool:
    for t in timeinfo:
        if t.count(':') != 0:
            time = list(map(str, t.split(':')))
        else:
            date = list(map(str, t.split('.')))


    if len(date) == 3:
        year = date[2]
    else:
        year = datetime.date.today().year
    month = int(date[1])
    day = int(date[0])

    hour = int(time[0])
    minute = int(time[1])

    try:
        newDate = datetime.datetime(year, month, day, hour, minute)
        correct_date = True
    except ValueError:
        correct_date = False

    if datetime.datetime(year, month, day, hour, minute) - datetime.datetime.now() >= 0 :
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
        year = date[2]
    else:
        year = datetime.date.today().year
    month = date[1]
    day = date[0]

    hour = time[0]
    minute = time[1]

    dt = datetime.datetime(year, month, day, hour, minute)
    return (dt - datetime.datetime(1970,1,1)).total_seconds()


def from_unix(unixtime):
    return datetime.datetime.fromtimestamp(unixtime)




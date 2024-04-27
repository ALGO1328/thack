import datetime

logs = open('logs.txt', 'w')

def checkdate(timeinfo) -> bool:
    for t in timeinfo:
        if t.count(':') != 0:
            time  = t.split(':')
        else:
            date = t.split('.')


    if len(date == 3):
        year = date[2]
    else:
        year = datetime.date.today().year
    month = date[1]
    day = date[0]

    hour = time[0]
    minute = time[1]


    try:
        newDate = datetime.datetime(year, month, day, hour, minute)
        correctDate = True
    except ValueError:
        correctDate = False
    return correctDate






def tounix(timeinfo) -> int:



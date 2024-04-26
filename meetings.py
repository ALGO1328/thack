import datetime
import calendar

import pytz


class Meeting:
    def __init__(self, time, link, creator):
        if time:
            self.time = time
        else:
            self.time = datetime.datetime.now()

        self.link = link
        self.creator = creator

    def get_info(self):
        now = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
        datetime.time
        return f''

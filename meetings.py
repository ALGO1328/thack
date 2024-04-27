import datetime

import time

import pytz

import dateconv


class Meeting:
    def __init__(self):
        self.time = None
        self.link = None
        self.creator = None
        self.members = None

    def add_link(self, link: str):
        self.link = link

    def add_time(self, time: int):
        self.time = time

    def add_creator(self, creator: str):
        self.creator = creator

    def add_members(self, members):
        self.members = members

    def get_info(self) -> str:
        event_time = dateconv.from_unix(self.time)
        dt = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
        unix_now = int((dt - datetime.datetime(1970, 1, 1)).total_seconds())
        time_to_event = str(datetime.timedelta(seconds=self.time - unix_now))

        return (f'{self.creator} приглашает вас на встречу, '
                f'дата: {datetime.date(event_time).strftime("%d.%m.%y")}, '
                f'в {datetime.datetime(event_time).strftime("%H:%M")}' 
                f'(через: {time_to_event} )')

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

    def add_time(self, time):
        if time is None or time == 0:
            self.time = datetime.datetime.now(pytz.timezone('Europe/Moscow')).timestamp()
        else:
            self.time = time

    def add_creator(self, creator: str):
        self.creator = creator

    def add_members(self, members):
        self.members = members

    def get_info(self) -> str:
        meeting_time = dateconv.from_unix(self.time)
        now_sec = int(datetime.datetime.now(pytz.timezone('Europe/Moscow')).timestamp())
        time_diff = self.time - now_sec
        return (f'Вы приглашены на онлайн встречу: {meeting_time.strftime('%d.%m %H:%M')} '
                f'\nСсылка: {self.link} '
                f'\nОрганизатор:{self.creator} '
                f'\nУчастники: {', '.join(self.members)} '
                f'\nНачало через 30 мин.')

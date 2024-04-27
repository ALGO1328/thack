import datetime

import time

import pytz


class Meeting:
    def __init__(self):
        self.time = None
        self.link = None
        self.creator = None
        self.members = None

    def add_link(self, link):
        self.link = link

    def add_time(self, time):
        self.time = time

    def add_creator(self, creator):
        self.creator = creator

    def add_members(self, members):
        self.members = members

    def get_info(self) -> str:  # Вас прглашает на встречу .. .. . (через #TODO
        now = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
        unix_time = time.mktime(now.timetuple())
        last_time = self.time - unix_time

        if int(last_time.strftime('%d')) == 0 and int(last_time.strftime('%m')) == 0:
            last_time = last_time.strftime('%H час. %M мин.')
        elif int(last_time.strftime('%m')) == 0 and int(last_time.strftime('%d')) != 0:
            last_time = last_time.strftime('%d д. %H час. %M мин.')
        else:
            last_time = last_time.strftime('%d д. %H час. %M мин.')
        return (f'Вас приглашает на встречу {self.creator}, '
                f'дата: {datetime.datetime.fromtimestamp(self.time, datetime.UTC).strftime('%d.%m.%Y')} '
                f'в {datetime.datetime.fromtimestamp(self.time, pytz.timezone('Europe/Moscow')).strftime('%H:%M')} '
                f'(через: {last_time} )')

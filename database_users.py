import datetime

import sqlite3

import pytz

import telebot.types

logs = open('logs.txt', 'w')


def database_connect() -> bool:
    try:
        conn = sqlite3.connect('database.db')
        return True
    except sqlite3.Error as e:
        return False


def add_member_to_base(userinfo: telebot.types.Message) -> bool:
    '''+ к базе userinfo.chat.id - id пользователя
    userinfo.from_user.username - юзернейм
    '''
    pass


def check_user_exist(userinfo: telebot.types.Message) -> bool:
    return True
    pass


def register_user(userinfo: telebot.types.Message) -> bool:
    pass


def add_schedule(userinfo: telebot.types.Message) -> bool:
    pass


...

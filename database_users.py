import datetime

import sqlite3

import pytz

import telebot.types

logs = open('logs.txt', 'w')

now = datetime.datetime.now(pytz.timezone("Europe/Moscow"))

conn = sqlite3.connect('database.db')

def database_connect() -> bool:
    try:
        logs.write(now.strftime("%Y-%m-%d %H:%M:%S") + '\n')
        return True
    except sqlite3.Error as e:
        return False

def check_user_exist(userinfo: telebot.types.Message) -> bool:
    return True
    pass


def register_user(userinfo: telebot.types.Message) -> bool:
    try:
        c = conn.cursor()
        c.execute("INSERT INTO users (id, name) VALUES (userinfo.chat.id, userinfo.from_user.username)")
        logs.write(now.strftime("%Y-%m-%d %H:%M:%S") + '\n')
        return True
    except sqlite3.Error as e:
        return False


def add_meeting(creator, time, URL) -> bool:
    try:
        c = conn.cursor
        c.execute("INSERT INTO meetings (time, creator, URL) VALUES (time, creator, URL)")
        logs.write(now.strftime("%Y-%m-%d %H:%M:%S") + '\n')
        return True
    except sqlite3.Error as e:
        return False



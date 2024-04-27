import datetime

import sqlite3

import pytz

import telebot.types

logs = open('logs.txt', 'w')

conn = sqlite3.connect('database.db')


def database_connect() -> bool:
    now = datetime.datetime.now(pytz.timezone("Europe/Moscow"))
    try:
        conn = sqlite3.connect('database.db')
        logs.write(now.strftime("%H:%M:%S") + 'Успешно подключено' + '\n')
        return True
    except sqlite3.Error as e:
        logs.write(now.strftime("%H:%M:%S") + 'Ошибка подключения к базе' + '\n')
        return False


def add_meeting(creator, time, link) -> bool:
    try:
        c = conn.cursor()
        c.execute("INSERT INTO meetings (time, creator, URL) VALUES (?, ?, ?)", (time, creator, link))
        conn.commit()
        return True
    except:
        return False

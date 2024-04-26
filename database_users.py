import datetime

import sqlite3

import pytz

import telebot.types

logs = open('logs.txt', 'w')

#TEMP


def database_connect() -> bool:
    try:
        conn = sqlite3.connect('database.db')
        return True
    except sqlite3.Error as e:
        return False

''' DATABASE CREATOR
def create_database():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE users
                 (id TEXT PRIMARY KEY NOT NULL,
                  name TEXT NOT NULL)''')

    c.execute('''CREATE TABLE meetings
                (time DATE PRIMARY KEY NOT NULL,
                creator TEXT NOT NULL, 
                URL TEXT NOT NULL)''')
'''

def add_member_to_base(userinfo: telebot.types.Message) -> bool:
    c = conn.cursor()
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
create_database()
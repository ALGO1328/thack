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


def check_user_exist(user_id) -> bool:
    c = conn.cursor()
    c.execute(f"SELECT id FROM users WHERE id={user_id}")
    found_user_id = c.fetchall()
    if found_user_id:
        return True
    else:
        return False

def get_userid(uname: str) -> str:
    try:
        c = conn.cursor()
        c.execute(f"SELECT id FROM users WHERE name={uname}")
        user_id = c.fetchall()
        return(str(user_id))
    except sqlite3.Error as e:
        return('')


def register_user(userinfo: telebot.types.Message) -> bool:
    try:
        c = conn.cursor()
        c.execute(f"INSERT INTO users (id, name) VALUES (?, ?)",
                  (str(userinfo.chat.id), str(userinfo.from_user.username.lower()).replace('@', '')))
        conn.commit()
        return True
    except sqlite3.Error as e:
        return False


def check_user_exist_by_username(username) -> bool:
    c = conn.cursor()
    c.execute(f"SELECT id FROM users WHERE name={str(username.replace('@', ''))}")
    found_id = c.fetchone()
    if found_id:
        return True
    else:
        return False

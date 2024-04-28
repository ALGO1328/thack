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
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(f"SELECT id FROM users WHERE id={user_id}")
    found_user_id = c.fetchall()
    if found_user_id:
        return True
    else:
        return False

def get_userid(uname: str):
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute(f"SELECT id FROM users WHERE name=?", (uname, ))
        user_id = c.fetchall()
        return(user_id)
    except:
        return('')


def register_user(userinfo: telebot.types.Message, mail) -> bool:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute(f"INSERT INTO users (id, name, mail) VALUES (?, ?, ?)",
                  (str(userinfo.chat.id), str(userinfo.from_user.username.lower()).replace('@', ''),
                   mail))
        conn.commit()
        return True


def check_user_exist_by_username(username) -> bool:
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(f"SELECT id FROM users WHERE name=?", (username, ))
    found_id = c.fetchall()
    if found_id:
        return True
    else:
        return False
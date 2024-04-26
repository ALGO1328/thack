import telebot

from telebot import types
from telebot.async_telebot import AsyncTeleBot

import telebot

import config

import asyncio

import datetime

import database_users


def main():
    @BOT.message_handler(commands=['register', 'reg', 'start'])
    async def register(message):
        if database_users.check_user_exist(message):
            await BOT.send_message(message.chat.id, text='Вы уже зарегистрированы! '
                                                         '\nВведите /instruct чтобы увидеть'
                                                         ' инструкции по созданию созвона')
        else:
            if database_users.register_user(message):
                time = datetime.datetime.now()
                try:
                    await BOT.send_message(message.chat.id, text='Вы успешно зарегистрировались')
                    await logs.write(f'{time.hour}:{time.minute}:{time.second}: Пользователь'
                                     f' {message.from_user.username} зарегистрирован успешно')
                except:
                    await logs.write(f'{time.hour}:{time.minute}:{time.second}: '
                                     f'Ошибка регистрации {message.from_user.username}')

    @BOT.message_handler(commands=['instructions', 'instruct', 'inst'])
    async def instructions(message):
        await BOT.send_message(message.chat.id, text=config.INSTRUCTIONS)

    @BOT.message_handler(commands=['meet'])
    async def meet(message):
        if not database_users.check_user_exist(message):
            await BOT.send_message(message.chat.id, text='Для начала Вам нужно зарегистрироваться командой /reg')
        c_args = list(map(str, message.text.split()))[1:]
        userlist = []
        for arg in c_args:

if __name__ == '__main__':
    BOT = AsyncTeleBot(token=config.TOKEN)
    logs = open('logs.txt', 'w')

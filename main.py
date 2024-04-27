import telebot

from telebot import types
from telebot.async_telebot import AsyncTeleBot

import telebot

import config

import asyncio

import datetime

from meetings import Meeting

import database_users


def main():

    async def get_meeting_link(*args):
        pass

    async def sendmeetinfo(meet: Meeting) -> bool:
        for user_id in meet.members:
            await BOT.send_message(user_id, text='вас приглашают...')

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
                                     f' {message.from_user.username} зарегистрирован успешно \n')
                except:
                    await logs.write(f'{time.hour}:{time.minute}:{time.second}: '
                                     f'Ошибка регистрации {message.from_user.username} \n')

    @BOT.message_handler(commands=['instructions', 'instruct', 'inst'])
    async def instructions(message):
        await BOT.send_message(message.chat.id, text=config.INSTRUCTIONS)

    @BOT.message_handler(commands=['meet'])
    async def meet(message):

        if not database_users.check_user_exist(message):
            await BOT.send_message(message.chat.id, text='Для начала Вам нужно зарегистрироваться командой /reg')
            return

        if '@' not in message.text or ' ' not in message.text or '/meet' not in message.text:
            await BOT.send_message(message.chat.id, text='Команда введена неверно')
            return

        tempdata.update({message.chat.id: {'usernameslist': list(),
                                           'timeargs': list(),
                                           'c_args': list(),
                                           'useridslist': list(),
                                           'meet': Meeting()}})
        tempdata[message.chat.id]['c_args'] = list(map(str, message.text.split()))[1:]
        for arg in tempdata[message.chat.id]['c_args']:
            if '@' in arg:
                tempdata[message.chat.id]['usernameslist'].append(arg)
            else:
                tempdata[message.chat.id]['timeargs'].append(arg)

        if not tempdata[message.chat.id]['timeargs']:
            tempdata[message.chat.id]['meet'].add_creator(message.chat.id)
            tempdata[message.chat.id]['meet'].add_link()


if __name__ == '__main__':
    tempdata = {}
    BOT = AsyncTeleBot(token=config.TOKEN)
    logs = open('logs.txt', 'w')

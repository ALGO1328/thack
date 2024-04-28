import telebot

from telebot import types

from telebot.async_telebot import AsyncTeleBot

import telebot

import config

import asyncio

import dateconv

import datetime

import pytz

from meetings import Meeting

import database_users

import asyncio


def main():

    def enter_email(message):
        if '@' in message.text:
            if database_users.register_user(message, message.text):
                BOT.send_message(message.chat.id, text='✅ Вы успешно зарегистрировались')
        else:
            BOT.send_message(message.chat.id, text='❗ Пожалуйста, введите почту корректно')
            BOT.register_next_step_handler(message, enter_email)

    def get_meeting_link(*args):
        return 'https://www.youtube.com'

    def sendmeetinfo(meet1: Meeting) -> bool:
        try:
            print(meet1.members)
            for username in meet1.members:
                BOT.send_message(chat_id=int(database_users.get_userid(username.replace('@', ''))[0][0]),
                                       text='1')
            return True
        except:
            return False

    @BOT.message_handler(commands=['register', 'reg', 'start'])
    def register(message):
        BOT.delete_message(message.chat.id, message.id)
        if database_users.check_user_exist(message.chat.id):
            BOT.send_message(message.chat.id, text='ℹ️ Вы уже зарегистрированы! '
                                                         '\nВведите /instruct чтобы увидеть'
                                                         ' инструкции по созданию созвона')
        else:
            BOT.send_message(message.chat.id, text='ℹ️ Введите свою основную почту (example@gmail.com)')
            BOT.register_next_step_handler(message, enter_email)


    @BOT.message_handler(commands=['instructions', 'instruct', 'inst'])
    def instructions(message):
        BOT.send_message(message.chat.id, text=config.INSTRUCTIONS)

    @BOT.message_handler(commands=['meet'])
    def meet(message):

        if not database_users.check_user_exist(message.chat.id):
            BOT.send_message(message.chat.id, text='ℹ️ Для начала Вам нужно зарегистрироваться командой /reg')
            return

        if '@' not in message.text or ' ' not in message.text or '/meet' not in message.text:
            BOT.send_message(message.chat.id, text='❗ Команда введена неверно, '
                                                         'используйте /inst для помощи в '
                                                         'написании команды')
            return

        tempdata.update({message.chat.id: {'members_list': list(),
                                           'timeargs': list(),
                                           'c_args': list(),
                                           'useridslist': list(),
                                           'meet': Meeting()}})

        tempdata[message.chat.id]['c_args'] = list(map(str, message.text.split()))[1:]

        for arg in tempdata[message.chat.id]['c_args']:
            if '@' in arg:
                tempdata[message.chat.id]['members_list'].append(arg)
            else:
                tempdata[message.chat.id]['timeargs'].append(arg)
            tempdata[message.chat.id]['members_list'].append(message.from_user.username)

        if not tempdata[message.chat.id]['timeargs']:
            tempdata[message.chat.id]['meet'].add_creator(message.chat.id)
            tempdata[message.chat.id]['meet'].add_link("youtube.com")  # тут добавляется ссылка на митинг вот оновот
            tempdata[message.chat.id]['meet'].add_members(tempdata[message.chat.id]['members_list'])
            for username in tempdata[message.chat.id]['members_list']:
                if not database_users.check_user_exist_by_username(username.replace('@', '')):
                    BOT.send_message(message.chat.id, text='❗ Не все приглашенные пользователи '
                                                                 'зарегистрировались в этом боте')
                    return
            if sendmeetinfo(tempdata[message.chat.id]['meet']):
                BOT.send_message(message.chat.id, text='ℹ️ Приглашения успешно отправлены')
            else: pass

        else:
            if not dateconv.checkdate(tempdata[message.chat.id]['timeargs']):
                BOT.send_message(message.chat.id, text='❗ Проверьте правильность ввода даты встречи '
                                                             'Используйте /inst для получения инструкции')
                return
            for username in tempdata[message.chat.id]['members_list']:
                if True:
                    BOT.send_message(message.chat.id, text='❗ Не все приглашенные пользователи '
                                                                 'зарегистрировались в этом боте')
                    return

    BOT.infinity_polling()


if __name__ == '__main__':
    tempdata = {}
    BOT = telebot.TeleBot(token=config.TOKEN)
    logs = open('logs.txt', 'w')
    main()

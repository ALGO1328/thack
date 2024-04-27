import telebot

from telebot import types

from telebot.async_telebot import AsyncTeleBot

import telebot

import config

import asyncio

import dateconv

import datetime

from meetings import Meeting

import database_users

import asyncio


async def main():

    async def get_meeting_link(*args):
        pass
    async def invited_users_checker(userlist):
        for username in userlist:
            if database_users.check_user_exist_by_username(username):
                pass

    async def sendmeetinfo(meet: Meeting) -> bool:
        try:
            for user_id in meet.members:
                await BOT.send_message(user_id, text=meet.get_info())
            return True
        except:
            return False

    @BOT.message_handler(commands=['register', 'reg', 'start'])
    async def register(message):
        await BOT.delete_message(message.chat.id, message.id)
        if database_users.check_user_exist(message.chat.id):
            await BOT.send_message(message.chat.id, text='ℹ️ Вы уже зарегистрированы! '
                                                         '\nВведите /instruct чтобы увидеть'
                                                         ' инструкции по созданию созвона')
        else:
            if database_users.register_user(message):
                time = datetime.datetime.now()
                try:
                    await BOT.send_message(message.chat.id, text='✅ Вы успешно зарегистрировались')
                    logs.write(f'{time.hour}:{time.minute}:{time.second}: Пользователь'
                               f' {message.from_user.username} зарегистрирован успешно \n')
                except:
                    logs.write(f'{time.hour}:{time.minute}:{time.second}: '
                               f'Ошибка регистрации {message.from_user.username} \n')

    @BOT.message_handler(commands=['instructions', 'instruct', 'inst'])
    async def instructions(message):
        await BOT.send_message(message.chat.id, text=config.INSTRUCTIONS)

    @BOT.message_handler(commands=['meet'])
    async def meet(message):

        if not database_users.check_user_exist(message.chat.id):
            await BOT.send_message(message.chat.id, text='ℹ️ Для начала Вам нужно зарегистрироваться командой /reg')
            return

        if '@' not in message.text or ' ' not in message.text or '/meet' not in message.text:
            await BOT.send_message(message.chat.id, text='❗ Команда введена неверно, '
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
            print(arg)
            if '@' in arg:
                tempdata[message.chat.id]['members_list'].append(arg)
            else:
                tempdata[message.chat.id]['timeargs'].append(arg)
        if not tempdata[message.chat.id]['timeargs']:
            tempdata[message.chat.id]['meet'].add_creator(message.chat.id)
            tempdata[message.chat.id]['meet'].add_link(get_meeting_link())
            tempdata[message.chat.id]['meet'].add_members(tempdata[message.chat.id]['members_list'])
            if not(invited_users_checker(tempdata[message.chat.id]['members_list'])):
                await BOT.send_message(message.chat.id, text='Не все пользователи зарегистрировались в этом боте')
        else:
            dateconv.checkdate(tempdata[message.chat.id]['timeargs'])
            dateconv.tounix(tempdata[message.chat.id]['timeargs'])

    await BOT.infinity_polling()


if __name__ == '__main__':
    tempdata = {}
    BOT = AsyncTeleBot(token=config.TOKEN)
    logs = open('logs.txt', 'w')
    asyncio.run(main())

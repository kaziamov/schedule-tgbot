#!/usr/bin/env python
import json
from aiogram import Bot, Dispatcher, executor

from settings import TOKEN as API_TOKEN, START_MESSAGE
from schedule import get_sections, schedule_for_day, schedule_for_section
from keyboards import make_keyboard, remove_keyboard
from commands import bot_commmands


def make_hello_message(options, desc='desc'):
    return "\n".join([f"{value[desc]}: /{key}" for key, value in options.items()])

# async def get_message():
#     return await


async def make_action(message, output_message, menu):
    await message.reply(output_message, reply_markup=menu)


async def start(message):
    """This handler will be called when user sends `/start` command"""
    await message.reply(hello_message, reply_markup=del_menu)

async def by_days(message):
    """This handler will be called when user sends `/start` command"""
    await message.reply("Выберите день:", reply_markup=keyboard_days)

async def by_section(message):
    """This handler will be called when user sends `/start` command"""
    await message.reply("Выберите секцию:", reply_markup=keyboard_sections)

async def schedule(message):
    """This handler will be called when user sends `/schedule` command"""
    await message.reply("Schedule", reply_markup=del_menu)

bot_commmands = {
    "by_days": {"categories": ['filter'], 'desc': "Посмотреть расписание по дням", 'action': by_days},
    "by_section": {"categories": ['filter'], "desc": "Узнать расписание секции", 'action': by_section},
    "start": {"categories": [], "desc": "Показать стартовое сообщение", 'action': start},
    "help": {"categories": [], "desc": "Помощь по командам бота", 'action': start},
    # "schedule": {"categories": ['filter'], "desc": "Узнать расписание секции", 'action': schedule},
    }

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

options = bot_commmands
hello_message = """{}
{}""".format(START_MESSAGE, make_hello_message(options))

menu = make_keyboard(bot_commmands, commands=["by_days", 'by_section'])
del_menu = remove_keyboard()

sections = get_sections()
keyboard_sections = make_keyboard(sections)

days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Субботы', 'Воскресенье']
keyboard_days = make_keyboard(days)


commands = list(bot_commmands.keys())



@dp.message_handler()
async def get_answer(message):
    if message.is_command():
        command = message.get_command()[1:]
        return await bot_commmands[command]['action'](message)
    else:
        text = message.md_text
        if text in days:
            responce = schedule_for_day(text)
            if not responce:
                responce = 'Нет занятий в этот день'
            return await make_action(message, responce, remove_keyboard)
        elif text in sections:
            responce = schedule_for_section(text)
            if responce:
                responce = 'Занятий не найдено'
            return await make_action(message, responce, remove_keyboard)
        else:
            await message.reply('Я тоже не умею ничего говорить')


if __name__ == '__main__':
    # print(schedule_for_day("Вторник"))
    # print(schedule_for_section('карате'))
    executor.start_polling(dp, skip_updates=False)

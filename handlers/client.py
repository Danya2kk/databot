from aiogram import Dispatcher, types
from buttons import kb_main
from aiogram.dispatcher.filters import Text


async def start(message: types.Message):
    await message.reply("Let's go", reply_markup=kb_main)


async def help(message: types.Message):
    answer = '''
/start - open keyboard
Day - output of the day by date (year.month.day)
Hide keyboard - hide keyboard
Help - help
                    '''
    await message.reply(answer, reply_markup=kb_main)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(help, Text(equals='Help', ignore_case=True))
import datetime
from aiogram import Dispatcher, types
from database import table


async def date(message: types.Message):
    parsed_message = message.text[5:].split('.')
    if len(parsed_message) == 3:
        list = []
        list.append(int(parsed_message[0]))
        list.append(int(parsed_message[1]))
        list.append(int(parsed_message[2]))
        date = datetime.datetime(list[0], list[1], list[2])
        date = date.ctime()
        day = table.selectName(date[0:3])
        answer = 'It is' + ' ' + day
    await message.reply(answer)


async def help(message: types.Message):
    answer = '''
/day - вывод дня по дате (год.месяц.день)
/help - помощь
                    '''
    await message.reply(answer)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(date, commands=['day'])
    dp.register_message_handler(help, commands=['help'])
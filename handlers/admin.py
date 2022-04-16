import datetime
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import table


class FSMAdmin(StatesGroup):
    date = State()


async def day(message: types.Message):
    await FSMAdmin.date.set()
    await message.reply("Введите дату(год.месяц.день)")


async def send_day(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
        day = data.get('date')
        parsed_message = day.split('.')
        if len(parsed_message) == 3:
            list = []
            list.append(int(parsed_message[0]))
            list.append(int(parsed_message[1]))
            list.append(int(parsed_message[2]))
            date = datetime.datetime(list[0], list[1], list[2])
            date = date.ctime()
            day = table.selectName(date[0:3])
            answer = 'It is' + ' ' + day
            await message.answer(answer)
    await state.finish()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(day, commands=['day'], state=None)
    dp.register_message_handler(send_day, state=FSMAdmin.date)



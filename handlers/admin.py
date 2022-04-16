import datetime
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import table
from aiogram.types import ReplyKeyboardRemove
from buttons import kb_main, kb_cancel
from aiogram.dispatcher.filters import Text


class FSMAdmin(StatesGroup):
    date = State()


async def hide(message: types.Message):
    await message.reply("Keyboard was hidden, enter /start to open keyboard again ", reply_markup=ReplyKeyboardRemove())


async def day(message: types.Message):
    await FSMAdmin.date.set()
    await message.reply("Enter the date(year.month.day)", reply_markup=kb_cancel)


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
            await message.answer(answer, reply_markup=kb_main)
    await state.finish()


async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("Cancellation was successful", reply_markup=kb_main)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(day, Text(equals='Day', ignore_case=True), state=None)
    dp.register_message_handler(cancel, Text(equals='Cancel', ignore_case=True), state='*')
    dp.register_message_handler(send_day, state=FSMAdmin.date)
    dp.register_message_handler(hide, Text(equals='Hide Keyboard', ignore_case=True))


from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_day = KeyboardButton('Day')   # создание объекта кнопки
button_hide_kb = KeyboardButton('Hide keyboard')
button_help = KeyboardButton('Help')

kb_main = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_main.add(button_day).insert(button_help).add(button_hide_kb)

button_cancel = KeyboardButton('Cancel')

kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel.add(button_cancel)
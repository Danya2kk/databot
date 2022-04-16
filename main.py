import logging
from create_bot import dp
from aiogram import executor
from handlers import client, admin

logging.basicConfig(level=logging.INFO)

admin.register_handlers(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
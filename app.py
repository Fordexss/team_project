import logging
import handlers
from loader import dp, db_bot, db_user
from utils.set_bot_commands import set_default_commands
from aiogram import executor
from utils.notify_admins import on_startup_notify


async def on_startup(dispatcher):
    db_bot.open()
    db_user.connect(db_bot)
    db_user.create_default_table()
    logging.info("Db has opened connection")
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)


async def on_shutdown(dispatcher):
    db_bot.close()
    logging.info("Db has closed connection")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)

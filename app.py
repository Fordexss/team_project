import logging
import handlers
<<<<<<< HEAD
from loader import dp, db_bot, db_user, db_parse
=======
from loader import dp, db_bot, db_user, db_question
>>>>>>> origin/master
from utils.set_bot_commands import set_default_commands
from aiogram import executor
from utils.notify_admins import on_startup_notify
from handlers.users.initial_test import init_questions


async def on_startup(dispatcher):
    db_bot.open()
    db_user.connect(db_bot)
    db_user.create_default_table()
<<<<<<< HEAD
    db_parse.connect(db_bot)
=======
    db_question.connect(db_bot)
    db_question.initialize_database()
    init_questions()
>>>>>>> origin/master
    logging.info("Db has opened connection")
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)


async def on_shutdown(dispatcher):
    db_bot.close()
    logging.info("Db has closed connection")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)

from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from parser.pars_gram import pars_gram
from parser.pars_lex import pars_lex


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)
    await pars_gram(dp)
    await pars_lex(dp)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)


from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from utils.db_api.db import BotDB
from utils.db_api.db_parse import LearnInfo 
from utils.db_api.db_user import DbUserInterface

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db_bot = BotDB(config.DB_FILE)
db_user = DbUserInterface()
db_parse = LearnInfo()
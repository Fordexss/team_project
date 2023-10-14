from environs import Env

env = Env()
env.read_env()  # читання змінних середовища

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
DB_FILE = env.str("DB_FILE")
DB_PARSE = env.str("DB_PARSE")


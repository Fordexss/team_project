from environs import Env

env = Env()
env.read_env()  # читання змінних середовища

DB_FILE = env.str("DB_FILE")
DRIVER = env.str("DRIVER_PATH")

import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

from loader import dp
from states import RegistrationStates

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS учні
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   last_name TEXT,
                   phone_number TEXT)''')
conn.commit()
conn.close()


async def save_user_data(data, user_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO учні (name, last_name, phone_number) VALUES (?, ?, ?)",
                   (data['name'], data['last_name'], data['phone_number']))
    conn.commit()
    conn.close()


@dp.message_handler(Command('start'))
async def cmd_start(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item = KeyboardButton("Відправити мої дані")
    markup.add(item)

    await message.reply("Вас вітаємо! Перед тим як продовжити, натисніть кнопку 'Відправити мої дані'.",
                        reply_markup=markup)

    await RegistrationStates.NAME.set()


@dp.message_handler(lambda message: message.text == "Відправити мої дані", state=RegistrationStates.NAME)
async def process_registration(message: types.Message):
    markup = types.ReplyKeyboardRemove()
    await message.reply("Для подальшого введіть ваше ім'я:", reply_markup=markup)

    await RegistrationStates.NAME.set()


@dp.message_handler(lambda message: message.text, state=RegistrationStates.NAME)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

        await message.reply("Тепер введіть ваше прізвище:")

        await RegistrationStates.LASTNAME.set()


@dp.message_handler(lambda message: message.text, state=RegistrationStates.LASTNAME)
async def process_lastname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['last_name'] = message.text

        await message.reply("І, нарешті, введіть ваш номер телефону:")

        await RegistrationStates.PHONE.set()


@dp.message_handler(lambda message: not message.text.isdigit(), state=RegistrationStates.PHONE)
async def process_phone_invalid(message: types.Message):
    return await message.reply("Номер телефону повинен бути числом. Спробуйте ще раз.")


@dp.message_handler(lambda message: message.text.isdigit(), state=RegistrationStates.PHONE)
async def process_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text

        await save_user_data(data, message.from_user.id)

        await message.reply("Дані відправлено та збережено в базі даних. Дякуємо за реєстрацію!",
                            reply_markup=ReplyKeyboardRemove())

    await state.finish()

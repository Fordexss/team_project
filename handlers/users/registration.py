import random
import string

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InputFile
from captcha.image import ImageCaptcha

from loader import dp, db_user
from states import RegistrationStates

captcha = ImageCaptcha(width=450, height=200)

CAPTCHA_IMAGE_PATH = "captcha.png"


async def send_captcha_image(user_id, message, state):
    captcha_text = ''.join(random.choices(string.ascii_letters + string.digits, k=5))

    captcha_image = captcha.generate(captcha_text)

    async with state.proxy() as state_data:
        state_data['captcha'] = captcha_text

    with open(CAPTCHA_IMAGE_PATH, 'wb') as image_file:
        image_file.write(captcha_image.read())

    # Відправляємо зображення капчі як InputFile
    with open(CAPTCHA_IMAGE_PATH, 'rb') as image_file:
        await message.reply_photo(InputFile(image_file),
                                  caption=f"Дані відправлено та збережено в базі даних. "
                                          f"Дякуємо за реєстрацію!\n"
                                          f"Перед завершенням реєстрації",
                                  reply_markup=ReplyKeyboardRemove())


@dp.message_handler(commands=['start'], state="*")  # Обробка будь якого стану
async def start_command(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    if not db_user.user_exists(user_id):
        markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item = KeyboardButton("Відправити мої дані")
        markup.add(item)

        await message.reply("Вас вітаємо! Перед тим як продовжити, натисніть кнопку 'Відправити мої дані'.",
                            reply_markup=markup)

        await RegistrationStates.NAME.set()
    else:
        await message.reply("Ви вже зареєстровані. Дякуємо!")


@dp.message_handler(lambda message: message.text == "Відправити мої дані", state=RegistrationStates.NAME)
async def process_registration(message: types.Message):
    markup = ReplyKeyboardRemove()
    await message.reply("Для подальшого введіть ваше ім'я:", reply_markup=markup)

    await RegistrationStates.NAME.set()


@dp.message_handler(lambda message: message.text.isalpha(), state=RegistrationStates.NAME)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

        await message.reply("Тепер введіть ваше прізвище:")

        await RegistrationStates.LASTNAME.set()


@dp.message_handler(lambda message: not message.text.isalpha(), state=RegistrationStates.NAME)
async def process_name_invalid(message: types.Message):
    return await message.reply("Ім'я повинно містити тільки букви. Повторіть ще раз:")


@dp.message_handler(lambda message: message.text.isalpha(), state=RegistrationStates.LASTNAME)
async def process_lastname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['last_name'] = message.text

        await message.reply("І, нарешті, введіть ваш номер телефону (тільки цифри):")

        await RegistrationStates.PHONE.set()


@dp.message_handler(lambda message: not message.text.isalpha(), state=RegistrationStates.LASTNAME)
async def process_lastname_invalid(message: types.Message):
    return await message.reply("Прізвище повинно містити тільки букви. Повторіть ще раз:")


@dp.message_handler(lambda message: not message.text.isdigit(), state=RegistrationStates.PHONE)
async def process_phone_invalid(message: types.Message):
    return await message.reply("Номер телефону повинен бути числом. Спробуйте ще раз.")


@dp.message_handler(lambda message: message.text.isdigit(), state=RegistrationStates.PHONE)
async def process_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text

    # Оновлюємо стан до RegistrationStates.CAPTCHA
    await RegistrationStates.CAPTCHA.set()

    # Відправляємо зображення капчі
    await send_captcha_image(message.from_user.id, message, state)


@dp.message_handler(lambda message: True, state=RegistrationStates.CAPTCHA)
async def process_captcha(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    async with state.proxy() as data:
        correct_captcha = data.get('captcha')
        attempts_left = data.get('attempts_left', 3)

        if message.text.lower() == correct_captcha.lower():
            db_user.save_user_data(data, user_id)
            await message.reply("Капчу введено вірно. Реєстрація завершена!",
                                reply_markup=ReplyKeyboardRemove())
            await state.finish()
        else:
            attempts_left -= 1
            if attempts_left > 0:
                data['attempts_left'] = attempts_left
                await message.reply(f"Капчу введено невірно. Залишилося спроб: {attempts_left}. "
                                    f"Спробуйте ще раз:")
            else:
                await message.reply("Ви вичерпали всі спроби. Реєстрація відхилена")
                await state.finish()

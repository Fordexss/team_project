from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, db_user
from states import RegistrationStates


@dp.message_handler(commands=['remove_me'], state="*")
async def remove_user(msg: types.Message):
    user_id = msg.from_user.id

    if db_user.user_exists(user_id):
        # Питаємо користувача, чи він впевнений у видаленні
        await msg.reply("Ви впевнені, що хочете видалити свій аккаунт? Ця дія не може бути скасована.\n"
                        "Відповідь 'Так' для підтвердження або 'Ні' для скасування.")

        # Встановлюємо стан підтвердження
        await RegistrationStates.CONFIRMATION_STATE.set()
    else:
        # Якщо аккаунту немає в базі даних
        await msg.reply("Видалення аккаунта неможливе, оскільки аккаунт не існує.")


@dp.message_handler(lambda message: message.text.lower() in ['так', 'ні'], state=RegistrationStates.CONFIRMATION_STATE)
async def handle_confirmation(msg: types.Message, state: FSMContext):
    user_id = msg.from_user.id

    async with state.proxy() as data:
        if msg.text.lower() == 'так':
            db_user.remove_user_from_db(user_id)
            await msg.reply("Ваш аккаунт успішно видалено.")
        elif msg.text.lower() == 'ні':
            await msg.reply("Видалення аккаунта скасовано.")

        await state.finish()

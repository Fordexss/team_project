from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp


@dp.message_handler(Command('info'), state="*")
async def bot_help(message: types.Message, state: FSMContext):
    text = ("Що може цей бот?🇬🇧🇬🇧🇬🇧",
            "Визначити твій рівень англійської\n"
            "Допомогти прокачати свої знання\n"
            "Давати рекомендації щодо вивчення нових слів та правил\n"
            "Давати завдання\n"
            "Допомогти тобі провести час із користю\n")

    await message.answer("\n".join(text))
    await state.finish()

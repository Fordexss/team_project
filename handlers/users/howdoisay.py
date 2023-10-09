from googletrans import Translator

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from keyboards.inline.keyboards_inline import language

from loader import dp
from states import HowDoISayStates

translator = Translator()

@dp.message_handler(commands='howdoisay')
async def choose_trans(message: types.Message):
    await message.answer('Виберіть мову для перекладу⬇️', reply_markup=language)

@dp.callback_query_handler(text='eng')
async def english_language(call: types.CallbackQuery):
    await call.message.answer(text='Введіть речення на англійській для перекладу на українську')
    await HowDoISayStates.Ukrainian.set()

@dp.callback_query_handler(text='ukr')
async def ukrainian_language(call: types.CallbackQuery):
    await call.message.answer(text='Введіть речення на українській для перекладу на англійську')
    await HowDoISayStates.English.set()

@dp.message_handler(state=HowDoISayStates.Ukrainian)
async def translate_eng(message: types.Message, state: FSMContext):
    frase = message.text
    translated_text_en = translator.translate(frase, src='en', dest='uk')
    await message.answer(f'Ось переклад ➡️ {translated_text_en.text}')
    await state.reset_state()

@dp.message_handler(state=HowDoISayStates.English)
async def translate_eng(message: types.Message, state: FSMContext):
    print('smth')
    frase = message.text
    translated_text_uk = translator.translate(frase, src='uk', dest='en')
    await message.answer(f'Ось переклад ➡️ {translated_text_uk.text}')
    await state.reset_state()

text_to_translate = "Hello, how are you?"
translated_text = translator.translate(text_to_translate, src='en', dest='es')

# Виведення результату перекладу
print(translated_text.text)




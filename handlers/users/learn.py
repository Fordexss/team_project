import sqlite3
import random

from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.keyboards_inline import general_choose, learning
from states.command_states import Learn


from utils.db_api.db_parse import LearnInfo

from loader import dp, db_parse, db_bot, grammar_text

LEVELS = ('A1', 'A2', 'B1', 'B2', 'C1')


@dp.message_handler(commands='learn')
async def start_learn(message: types.Message):
    await message.answer("Let's start learning")

    await message.answer('Choose how you want to study today⬇️',
                        reply_markup=general_choose)

# @dp.callback_query_handler(text='grm', state='*')
# async def format_grammar(call: types.CallbackQuery):
#     await call.message.answer(text='Which format you want to learn grammar⬇️',
#                                reply_markup=grammar_choose)
#     await Learn.Grammar.set()


max_message_length = 4096

@dp.callback_query_handler(text='grm1', state='*')
async def text_grammar(call: types.CallbackQuery):
    db_parse.user_score()
    user_id = int(call.from_user.id)
    level = db_parse.user_level(user_id)  
    if level in LEVELS:
        grammar_themes = db_parse.grammar(level)
        theme, text = random.choice(grammar_themes) 
        reply_text = f'<b>{theme}</b> \n\n{text}'
        await call.message.edit_text(text=reply_text[:max_message_length],
                                     parse_mode='html')
    else:
        await call.message.answer(text="Grammar text not found for this level.")

@dp.callback_query_handler(text='vid', state='*')
async def show_video(call: types.CallbackQuery):
    db_parse.user_score()
    user_id = int(call.from_user.id)
    level = db_parse.user_level(user_id)  
    if level in LEVELS:
        grammar_video = db_parse.video(level)
        theme, video = random.choice(grammar_video)
        text = f'<b>{theme}</b> \n\n{video}'
        await call.message.edit_text(text=text,
                                     parse_mode='html')
    else:
        await call.message.answer("Video not found for this level.")


@dp.callback_query_handler(text='new', state='*')
async def learn_lexic(call: types.CallbackQuery):
    user_id = int(call.from_user.id)
    level = db_parse.user_level(user_id)
    words_score = db_parse.words_quntity(user_id)
    if level in LEVELS:
        words = db_parse.lexic(level)
        for i in range(10):
            word, translate = random.choice(words)
            word_to_study = f'<u>{word}</u> - {translate}'
            await call.message.answer(text=word_to_study)
    else:
        await call.message.answer("Word not found for this level.")

# @dp.callback_query_handler(text='vid', state='*')
# async def english_language(call: types.CallbackQuery):
#     await call.message.answer(text=f'''Here is the video⬇️
#                               {pars_video()}''')

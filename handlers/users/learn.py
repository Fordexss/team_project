import sqlite3
import random

from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.keyboards_inline import general_choose, grammar_choose
from states.command_states import Learn

from parser.pars_gram import pars_grammar
from parser.pars_lex import pars_lexic
from parser.pars_vid import pars_video
from utils.db_api.db_parse import LearnInfo

from loader import dp, db_parse, db_bot, grammar_text

LEVELS = ('A1', 'A2', 'B1', 'B2', 'C1')

@dp.message_handler(commands='learn')
async def start_learn(message: types.Message):
    await message.answer("Let's start learning")

    await message.answer('Choose how you want to study today⬇️',
                        reply_markup=general_choose)

@dp.callback_query_handler(text='grm', state='*')
async def format_grammar(call: types.CallbackQuery):
    await call.message.answer(text='Which format you want to learn grammar⬇️',
                               reply_markup=grammar_choose)
    await Learn.Grammar.set()

@dp.callback_query_handler(text='grm1', state='*')
async def text_grammar(call: types.CallbackQuery):
    user_id = int(call.from_user.id)
    level = db_parse.user_level(user_id)  

    if level in LEVELS:
        grammar_text1 = db_parse.grammar_text(level)
        await call.message.answer(text=grammar_text1)
    else:
        await call.message.answer("Grammar text not found for this level.")
    # await call.message.answer(text=f'{LearnInfo.grammar_text(LearnInfo.user_level(user_id))}')


# @dp.callback_query_handler(text='new', state='*')
# async def english_language(call: types.CallbackQuery):
#     # await call.message.answer(text='Which format you want to learn grammar⬇️',
#     #                            reply_markup=grammar_choose)
    
# @dp.callback_query_handler(text='vid', state='*')
# async def english_language(call: types.CallbackQuery):
#     await call.message.answer(text=f'''Here is the video⬇️
#                               {pars_video()}''')

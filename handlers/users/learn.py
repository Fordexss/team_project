import sqlite3

from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.inline.keyboards_inline import general_choose, grammar_choose
from states.command_states import Learn

from parser.pars_gram import pars_grammar
from parser.pars_lex import pars_lexic
from parser.pars_vid import pars_video
from utils.db_api.db_parse import LearnInfo

from loader import dp, db_parse

@dp.message_handler(commands='learn')
async def start_learn(message: types.Message):
    await message.answer("Let's start learning")

    await message.answer('Choose how you want to study today⬇️',
                        reply_markup=general_choose)

@dp.callback_query_handler(text='grm', state='*')
async def format_grammar(call: types.CallbackQuery):
    await call.message.answer(text='Which format you want to learn grammar⬇️',
                               reply_markup=grammar_choose)
    # await Learn.Grammar.set()

# @dp.callback_query_handler(text='grm1', state='*')
# async def text_grammar(call: types.CallbackQuery):
#     await call.message.answer(text=f'{db_parse.grammar_text()}')


# @dp.callback_query_handler(text='new', state='*')
# async def english_language(call: types.CallbackQuery):
#     # await call.message.answer(text='Which format you want to learn grammar⬇️',
#     #                            reply_markup=grammar_choose)
    
# @dp.callback_query_handler(text='vid', state='*')
# async def english_language(call: types.CallbackQuery):
#     await call.message.answer(text=f'''Here is the video⬇️
#                               {pars_video()}''')

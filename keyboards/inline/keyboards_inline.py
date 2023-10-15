from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

language = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='English🗣', callback_data='eng')],
        [InlineKeyboardButton(text='Українська🗣', callback_data='ukr')]
    ]
)

general_choose = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Grammar🎓', callback_data='grm')],
        [InlineKeyboardButton(text='New words🗣', callback_data='new')],
        [InlineKeyboardButton(text='Video🎬', callback_data='vid')],
    ]
)

grammar_choose = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Message (text)💬', callback_data='grm1')],
        [InlineKeyboardButton(text='Video🎥', callback_data='grm2')],
    ]
)


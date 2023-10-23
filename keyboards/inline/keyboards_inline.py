from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

language = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='English🗣', callback_data='eng')],
        [InlineKeyboardButton(text='Українська🗣', callback_data='ukr')]
    ]
)

general_choose = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Grammar🎓', callback_data='grm1')],
        [InlineKeyboardButton(text='New words🗣', callback_data='new')],
        [InlineKeyboardButton(text='Video🎬', callback_data='vid')],
    ]
)

learning = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='I have learned', callback_data='hle')],
        [InlineKeyboardButton(text='Back', callback_data='bak')],
    ]
)


# grammar_choose = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [InlineKeyboardButton(text='Message (text)💬', callback_data='grm1')],
#         [InlineKeyboardButton(text='Video🎥', callback_data='grm2')],
#     ]
# )


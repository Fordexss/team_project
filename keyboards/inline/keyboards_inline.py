from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

language = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='English🗣', callback_data='eng')],
        [InlineKeyboardButton(text='Українська🗣', callback_data='ukr')]
    ]
)
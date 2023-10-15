from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def details(lvl):
    details_in_kb = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text='Відповіді тесту', callback_data='answers')],
            ],
            resize_keyboard=True,
        )
    if lvl != 'Ви ще зовсім початківець!':
        details_in_kb.add(InlineKeyboardButton(text='Про мій рівень', callback_data='about_lvl'))
    return details_in_kb

main_page_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton('Головна', callback_data='main')]
    ]
)

prev_button = InlineKeyboardButton('Попередня', callback_data='prev_page')
next_button = InlineKeyboardButton('Наступна', callback_data='next_page')

def answers_markup(buttons):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[buttons, [InlineKeyboardButton('Головна', callback_data='main')]],
    )
    return markup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def dynamic_reply_kb(quiz_button):
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=quiz_button[i], callback_data=0) for i in range(0, 3)]
        ],
        resize_keyboard=True,
    )


sure_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Звісно!')],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

yes_n_no = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Так'), KeyboardButton('Ні')],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
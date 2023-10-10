from aiogram.dispatcher.filters.state import StatesGroup, State


class RegistrationStates(StatesGroup):
    CURRENT_STATE = State()
    NAME = State()
    LASTNAME = State()
    PHONE = State()
    CAPTCHA = State()
    CONFIRMATION_STATE = State()
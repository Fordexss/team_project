from aiogram.dispatcher.filters.state import StatesGroup, State


class RegistrationStates(StatesGroup):
    CURRENT_STATE = State()
    NAME = State()
    LASTNAME = State()
    PHONE = State()
    CAPTCHA = State()
    CONFIRMATION_STATE = State()


# for howdoisay
class HowDoISayStates(StatesGroup):
    Ukrainian = State()
    English = State()


# for learn
class Learn(StatesGroup):
    Grammar = State()
    Words = State()
    Video = State()

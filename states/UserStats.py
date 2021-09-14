from aiogram.dispatcher.filters.state import State, StatesGroup


# Stats
class Form(StatesGroup):
    Phone = State()
    SuppotLoginSelect = State()
    LoginEnter = State()
    PasswordEnter = State()
    AuthMongo = State()
    SetLang = State()
    GetPhoto = State()
    TextToBraille = State()
    Menu = State()
    Sample = State()
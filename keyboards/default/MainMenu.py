from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

set_lang_def = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔄Tilni tanlash"),
        ],
    ],
    resize_keyboard=True,
)

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📝Отправить картинку"),
        ],
    ],
    resize_keyboard=True,
)
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
            KeyboardButton(text="↪️ Ortga qaytish")
        ],
    ],
    resize_keyboard=True,
)

set_settings = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Braille -> Text"),
            KeyboardButton(text="Text -> Braille")
        ]
    ],
    resize_keyboard=True
)
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

set_lang = InlineKeyboardMarkup(
    keyboard=[
        [
            InlineKeyboardButton(text="Russian", callback_data='RU'),
            InlineKeyboardButton(text="English", callback_data='EN'),
        ],
        [
            InlineKeyboardButton(text="Uzbek (cyrillic)", callback_data='UZ'),
            InlineKeyboardButton(text="Uzbek (latin)", callback_data='UZL'),
        ],
        [
            InlineKeyboardButton(text="Latvian", callback_data='LV'),
            InlineKeyboardButton(text="Greek", callback_data='GR'),
        ],
    ],
    resize_keyboard=True,
)
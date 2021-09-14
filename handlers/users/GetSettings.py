from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default import main_menu, set_settings
from loader import dp
from states.UserStats import Form


@dp.message_handler(text="Braille -> Text")
async def set_settings(msg: types.Message):
    await msg.answer("Braille alifbosida yozilgan rasmni yuborish uchun bosing!", reply_markup=main_menu)
    await Form.GetPhoto.set()

@dp.message_handler(text="Text -> Braille")
async def set_settings(msg: types.Message):
    await msg.answer("Braillega o'tkazish kerak bo'lgan rasmni yuboring!", reply_markup=main_menu)
    await Form.TextToBraille.set()

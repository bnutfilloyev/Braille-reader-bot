from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import aiogram.utils.markdown as md
from loader import dp, bot
from states.UserStats import Form
from aiogram.dispatcher import FSMContext
# from utils.notify_admins import on_start_command_notify


@dp.message_handler(CommandStart(), state='*')
async def process_authorization(message: types.Message, state: FSMContext):

    await message.answer("Добро пожаловать!")
    await Form.Phone.set()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    reg_button = types.KeyboardButton(text='Отправить номер', request_contact=True)
    keyboard.add(reg_button)


    await message.answer(
        md.text(
            md.text("Нажмите, чтобы отправить номер"),
            sep='\n',
        ),
        reply_markup=keyboard
    )

    # await on_start_command_notify(message)

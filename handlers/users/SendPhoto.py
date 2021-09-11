from aiogram import types
from aiogram.dispatcher import FSMContext
from uuid import uuid4
import os

from keyboards.default import main_menu
from loader import dp
from states.UserStats import Form

@dp.message_handler(text="📝Отправить картинку", state=Form.GetPhoto)
async def get_photo_message(msg: types.Message, state: FSMContext):
    await msg.answer("Отправить изображение Брайля", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(content_types='photo', state=Form.GetPhoto)
async def get_photo(message: types.Message, state: FSMContext):
    text = uuid4()

    await message.photo[-1].download('input/{}.jpg'.format(text))
    await message.answer("Фото принято\n\n"
                         "Подождите пожалуйста ...")

    os.system('python run_local.py -l EN -o input/{}.jpg output'.format(text))

    with open("output/{}.marked.jpg".format(text), 'rb') as photo:
        with open("output/{}.marked.txt".format(text), 'r') as txt:
            marc = txt.readlines()
            listToStr = ' '.join(map(str, marc))
            await message.answer_photo(photo=photo, caption=f"<code>{listToStr}</code>", reply_markup=main_menu)

        with open("output/{}.marked.brl".format(text), 'rb') as brl:
            await message.answer_document(brl)

        await state.finish()


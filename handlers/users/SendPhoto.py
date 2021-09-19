from aiogram import types
from aiogram.dispatcher import FSMContext
from uuid import uuid4
import os

from keyboards.default import main_menu, set_settings
from loader import dp, bot
from states.UserStats import Form
from braille_utils.braille import writeText
import requests
from data import mathpix
import json

@dp.message_handler(text="📝Отправить картинку", state=Form.GetPhoto)
async def get_photo_message(msg: types.Message):
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

@dp.message_handler(text="📝Отправить картинку", state=Form.TextToBraille)
async def get_photo_message(msg: types.Message):
    await msg.answer("Rasm yuboring!", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(content_types='photo', state=Form.TextToBraille)
async def get_photo(message: types.Message, state: FSMContext):
    text = uuid4()
    await message.photo[-1].download('input/{}.jpg'.format(text))
    r = mathpix.latex({
        'src': mathpix.image_uri('input/{}.jpg'.format(text)),
        'ocr': ['math', 'text'],
        'skip_recrop': True,
        'formats': ['text', 'latex_styled', 'asciimath', 'mathml'],
        'format_options': {
            'text': {
                'transforms': ['rm_spaces', 'rm_newlines'],
                'math_delims': ['$', '$']
            },
            'latex_styled': {'transforms': ['rm_spaces']}
        }
    })

    print("\nResult object: \n{}".format(json.dumps(r, indent=4, sort_keys=True)))
    with open(f"output/{text}.brl", 'w+') as f:
        f.writelines(writeText(r['asciimath']))
    with open(f"output/{text}.brl", 'rb') as f:
        send_text = f"<b>Photo text:</b> <code>{r['asciimath']}</code>\n\n"
        send_text += f"<b>Latex style</b>: <code>{r['latex_styled']}</code>\n\n"
        send_text += f"<b>Braille text:</b> <code>{writeText(r['asciimath'])}</code>\n"

        await message.answer_document(f, caption=send_text, )


@dp.message_handler(text="↪️ Ortga qaytish", state='*')
async def back_menu(msg: types.Message, state: FSMContext):
    await msg.answer("Iltimos tanlang", reply_markup=set_settings)
    await state.finish()
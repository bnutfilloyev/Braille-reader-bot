from loader import dp, bot
from keyboards.default.MainMenu import main_menu

# MongoDB init
from utils.db_api import users_db
from utils.db_api import profiles_db

# Init aiogram
import aiogram.utils.markdown as md
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor
from states.UserStats import Form

#for datetime
from datetime import datetime


@dp.message_handler(content_types=['contact'], state=Form.Phone)
async def contact_hand(message, state: FSMContext):
    textback = ""
    async with state.proxy() as data:
        data['phone'] = str(message.contact.phone_number).replace('+', '').replace(' ', '')
        req_db = users_db.update_one({'phone': data['phone']}, {'$set': {
            "phone": data['phone'],
            "updated": datetime.now()
            }
        }, upsert=True)

        if (req_db.matched_count):
            textback = "Я рад снова видеть Вас {}".format(dict(message['chat'])['first_name'])
        else:
            textback = "Добро пожаловать {}".format(dict(message['chat'])['first_name'])
    await Form.SuppotLoginSelect.set()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Войти")

    await bot.send_message(
        message.chat.id,
        md.text(
            md.text(textback),
            md.text("Нажмите Войти"),
            sep='\n',
        ),
        reply_markup=markup,
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(state=Form.Phone)
async def contact_hand(message):
    await bot.send_message(
        message.chat.id,
        md.text(
            md.text("Отправить номер"),
            sep='\n',
        ),
        parse_mode=ParseMode.MARKDOWN,
    )


@dp.message_handler(lambda message: message.text not in ["Войти"], state=Form.SuppotLoginSelect)
async def choose_invalid(message: types.Message):
    return await message.reply("Пожалуйста, выберите!")


@dp.message_handler(lambda message: message.text in ["Войти"], state=Form.SuppotLoginSelect)
async def process_SuppotLoginSelect(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['login'] = message.text
        print(data)
        await Form.LoginEnter.set()

        # And send message
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text("Введите логин"),
                sep='\n',
            ),
            reply_markup=types.ReplyKeyboardRemove(),
            parse_mode=ParseMode.MARKDOWN,
        )


@dp.message_handler(state=Form.LoginEnter)
async def process_LoginEnter(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['login'] = message.text

        await Form.PasswordEnter.set()

        # And send message
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text("Введите пароль"),
                sep='\n',
            ),
            reply_markup=types.ReplyKeyboardRemove(),
            parse_mode=ParseMode.MARKDOWN,
        )


@dp.message_handler(state=Form.PasswordEnter)
async def process_PasswordEnter(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['password'] = message.text

        await Form.AuthMongo.set()
        password = data['password']
        print(("GOT\nLogin: {}\npassword: {}\n").format(data['login'], password))

        profile_result = profiles_db.find_one(filter={'login': data['login'], 'password': password})
        if profile_result != None:
            profiles_db.find_and_modify({'login': data['login'], 'password': password},
                                        {'$set': {'last_login': datetime.now()}})
            await message.answer("{} вы зарегистрировались, выберите следующие разделы, чтобы использовать бот".format(message.from_user.full_name), reply_markup=main_menu)
            await state.finish()
        else:
            await Form.SuppotLoginSelect.set()
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
            markup.add("Войти")

            await bot.send_message(message.chat.id,
                                   md.text(md.text("Логин или пароль неверны, попробуйте еще раз!"),
                                           sep='\n', ), reply_markup=markup, parse_mode=ParseMode.MARKDOWN, )

        update_result = users_db.find_and_modify({"chat.id": message.chat.id}, {'$set': {'login': data['login']}})
        # print(update_result)



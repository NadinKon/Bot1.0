from aiogram import types, Dispatcher, Bot
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from jokes import list_jokes
from advice import list_advice

bot = Bot(token='5904419244:AAHcSXUE7Gc07YA1PkB0ihKFzTa7TrhQV')
dp = Dispatcher(bot)

b1 = KeyboardButton('/Анекдотик')
b2 = KeyboardButton('/Совет_дня')
b3 = KeyboardButton('/Сегодня')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1).row(b2, b3)



@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    name = message.from_user.first_name
    await bot.send_message(message.from_user.id, f'Привет {name}!', reply_markup=kb_client)
    await message.delete()


@dp.message_handler(commands=['Анекдотик'])
async def open_command(message: types.Message):
    await bot.send_message(message.from_user.id, list_jokes[0])
    del list_jokes[0]


@dp.message_handler(commands=['Совет_дня'])
async def place_command(message: types.Message):
    await bot.send_message(message.from_user.id, list_advice[0])


@dp.message_handler(commands=['Сегодня'])
async def menu_command(message : types.Message):
    await bot.send_message(message.from_user.id, list_advice[1])


@dp.message_handler()
async def new_message(message: types.Message):
    name = message.from_user.first_name
    if message.text:
        await message.answer('Я имею Вам кое-что сказать… Выбирай в меню!')


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(open_command, commands=['Анекдотик'])
    dp.register_message_handler(place_command, commands=['Совет_дня'])
    dp.register_message_handler(menu_command, commands=['Сегодня'])
    #dp.register_message_handler(new_message, content_types=types.ContentType.TEXT)


executor.start_polling(dp)
from aiogram import types, Dispatcher

from config import bot

#@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.message_handler(echo)
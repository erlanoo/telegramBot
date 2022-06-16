from aiogram import types, Dispatcher

from config import bot

#@dp.message_handler()
async def echo(message: types.Message):
    if message.text.startswith('pin'):
        await bot.pin_chat_message(message.chat.id,message.message_id)
    x = message.text
    try:
        x = int(x)
        c = 1
    except:
        pass
        c = 0
    if c == 1:
        await bot.send_message(message.chat.id, f"{x * x}")
    elif c == 0:
        await bot.send_message(message.chat.id, x)
    else:
        pass


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
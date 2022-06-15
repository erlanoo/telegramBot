from aiogram import types, Dispatcher
from config import bot


async def pin(message: types.Message, ADMIN):
    if message.from_user.id not in ADMIN:
        await message.reply("Вы не являетесь админоm в данной группе!")
    elif message.reply_to_message:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await bot.send_message(message.chat.id, 'Нужно ответить на сообщение чтобы его закрепить!')

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(pin)
from aiogram import types
from aiogram.utils import executor
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
import logging


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"hi, I'm a created bot")

@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "NEXT",
        callback_data='button_call_1'
    )
    markup.add(button_call_1)

    question = '. Какие две планеты вращаются в обратном направлении от остальных?'
    answers = [
        'Уран и Венера', 'Венера и Плутон', 'Меркурий и Юпитер', 'Земля и Нептун'
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="вопросы по Астраномии",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

@dp.callback_query_handler(lambda coll: coll.data == "button_call_1")
async def quez_2(coll: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton(
        "",
        callback_data='button_call_2'
    )
    markup.add(button_call_2)

    question = 'Когда Адольф Гитлер совершил самоубийтво?'
    answers = [
        '30-апреля,1945-году',
        '29-апреля,1945году',
        '28-апрель,1945-году',
        '1945-году'
    ]
    await bot.send_poll(
        chat_id=coll.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="сам думай",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

@dp.message_handler(commands=['mem'])
async def mem(message: types.CallbackQuery):
    photo = open('media/1-jxzx2-6ntms.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)

@dp.message_handler()
async def echo(message: types.Message):
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

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

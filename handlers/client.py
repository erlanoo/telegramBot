from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.client_kb import start_markup
from config import bot

#@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f"hi, I'm a created bot {message.from_user.full_name}",
                           reply_marup=start_markup)
# @dp.message_handler(commands=['quiz'])
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

#@dp.message_handler(commands=['mem'])
async def mem(message: types.CallbackQuery):
    photo = open('media/1-jxzx2-6ntms.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)

async def quiz3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call4 = InlineKeyboardButton("next", callback_data="button_call4")
    markup.add(button_call4)
    question1 = "В каком году ?"
    answers1 = ['да', 'нет', '2000', '20011']
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question1,
        options=answers1,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
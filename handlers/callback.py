from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

from config import bot


#@dp.callback_query_handler(lambda coll: coll.data == "button_call_1")
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

def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quez_2, lambda coll: coll.data == "button_call_1")
    #  dp.register_callback_query_handler(quez_3, lambda coll: coll.data == "button_call_2")




from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from decouple import config

storage = MemoryStorage()

TOKEN = ("5334581788:AAER-IeOiGBS7vns9uHzZOcu_BTZ6YxjdKM")

bot = Bot(TOKEN)

dp = Dispatcher(bot=bot, storage=storage)

ADMIN = [886271609]


from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import storage

storage = MemoryStorage()

bot = Bot(token='5934493051:AAFzHaTjoO6T6gPx6wtCZ4mBkFpVHvsmgqo')
dp = Dispatcher(bot, storage=storage)


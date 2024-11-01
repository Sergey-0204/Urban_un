from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import F
from aiogram.filters import Command
from aiogram import Router
import asyncio

API_TOKEN = '7640257355:AAFPhhP712ZU5THiI90jyEjFTvwgSdb_ZMc'  # Вставьте сюда ваш токен бота

# Создаем объекты Bot и Dispatcher
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)  # Передаем только storage в Dispatcher

# Создаем роутер для обработки команд
router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я бот.")

@router.message(F.text)
async def echo_message(message: types.Message):
    await message.answer(message.text)

# Подключаем роутер к диспетчеру
dp.include_router(router)

async def main():
    # Запуск бота
    await dp.start_polling(bot)  # Передаем bot в start_polling



if __name__ == "__main__":
    asyncio.run(main())
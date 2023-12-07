import asyncio
import logging
import sys
from aiogram import Bot, types, Dispatcher
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from config import TOKEN
from scheduler import api_requests
from threading import Thread

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message_handler()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("NT!")


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    thread = Thread(target=api_requests)
    thread.start()
    asyncio.run(main())

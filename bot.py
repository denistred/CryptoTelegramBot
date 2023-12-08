import asyncio
import logging
import sys
import time

from aiogram import Bot, Dispatcher
from aiogram.types import Message

from api_request import get_cryptocurrency
from helpers import volume_checker, write_json
from config import TOKEN, TG_ID

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Ваш id {message.from_user.id}!")


async def cripto_signal(id, response_json) -> None:
    current_names = list(response_json.keys())
    print(current_names)
    try:
        await bot.send_message(id, f"Найдено нужных криптовалют: {len(response_json)} ")

        while current_names:
            crypto_name = current_names.pop(0)
            msg = f"{crypto_name} - Изменение: {round(response_json[crypto_name]['change'], 2)}% - Капитализация: {int(response_json[crypto_name]['cap'])} USD\n"
            await bot.send_message(id, msg)

    except TypeError:
        pass


async def create_dp() -> None:
    await dp.start_polling(bot)


async def schedule_task() -> None:
    while True:
        await asyncio.sleep(60)
        current_time = time.localtime()
        if current_time.tm_min == 0 or current_time.tm_min == 30:
            api_response = get_cryptocurrency() # Получаем ответ от API
            changed_cryptos = volume_checker(current_time.tm_hour, current_time.tm_min, api_response) # Получаем имена нужных криптовалют
            write_json(api_response, current_time.tm_hour, current_time.tm_min) # Записываем полученные данные в json
            await cripto_signal(TG_ID, changed_cryptos)


async def main():
    tasks = [
        asyncio.create_task(create_dp()),
        asyncio.create_task(schedule_task()),
    ]

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

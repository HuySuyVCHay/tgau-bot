from os import getenv

import asyncio
import logging

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from app.utils.logger_config import setup_logger
from app.handlers import start, custom

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

setup_logger()
logger = logging.getLogger(__name__)

dp = Dispatcher()
dp.include_router(start.router)
dp.include_router(custom.router)


async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот остановлен")
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import get_settings
from database.db import init_db
from handlers import fallback, measurements, profile, start


async def main() -> None:
    logging.basicConfig(level=logging.INFO)
    settings = get_settings()

    if not settings.bot_token:
        raise RuntimeError("BOT_TOKEN не задан. Создайте .env на основе .env.example.")

    await init_db()

    bot = Bot(token=settings.bot_token)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(start.router)
    dp.include_router(measurements.router)
    dp.include_router(profile.router)
    dp.include_router(fallback.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

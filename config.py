from dataclasses import dataclass

from dotenv import load_dotenv
import os


load_dotenv()


@dataclass(frozen=True)
class Settings:
    bot_token: str
    database_url: str = "sqlite+aiosqlite:///style_bot.db"


def get_settings() -> Settings:
    return Settings(
        bot_token=os.getenv("BOT_TOKEN", ""),
        database_url=os.getenv("DATABASE_URL", "sqlite+aiosqlite:///style_bot.db"),
    )

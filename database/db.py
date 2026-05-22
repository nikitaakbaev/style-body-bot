from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from config import get_settings
from database.models import Base, UserProfile


settings = get_settings()

engine = create_async_engine(settings.database_url, echo=False)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def upsert_user_profile(
    *,
    telegram_id: int,
    username: str | None,
    bust: float,
    waist: float,
    hips: float,
    body_type: str,
) -> UserProfile:
    async with async_session_maker() as session:
        result = await session.execute(
            select(UserProfile).where(UserProfile.telegram_id == telegram_id)
        )
        profile = result.scalar_one_or_none()

        if profile is None:
            profile = UserProfile(
                telegram_id=telegram_id,
                username=username,
                bust=bust,
                waist=waist,
                hips=hips,
                body_type=body_type,
            )
            session.add(profile)
        else:
            profile.username = username
            profile.bust = bust
            profile.waist = waist
            profile.hips = hips
            profile.body_type = body_type

        await session.commit()
        await session.refresh(profile)
        return profile


async def get_user_profile(telegram_id: int) -> UserProfile | None:
    async with async_session_maker() as session:
        result = await session.execute(
            select(UserProfile).where(UserProfile.telegram_id == telegram_id)
        )
        return result.scalar_one_or_none()

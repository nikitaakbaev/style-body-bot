from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

from database.db import get_user_profile
from keyboards.main import main_keyboard, result_keyboard
from services.body_type_detector import detect_body_type
from services.recommendations import format_result_text


router = Router()


@router.message(F.text == "Мой результат")
@router.message(Command("result", "profile"))
async def show_profile(message: Message) -> None:
    if message.from_user is None:
        await message.answer("Не удалось определить пользователя.", reply_markup=main_keyboard())
        return

    profile = await get_user_profile(message.from_user.id)
    if profile is None:
        await message.answer(
            "Пока нет сохраненного результата. Давайте сначала рассчитаем тип фигуры.",
            reply_markup=main_keyboard(),
        )
        return

    detection = detect_body_type(
        bust=profile.bust,
        waist=profile.waist,
        hips=profile.hips,
    )
    await message.answer(format_result_text(detection), reply_markup=result_keyboard())

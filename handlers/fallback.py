from aiogram import Router
from aiogram.types import Message

from keyboards.main import main_keyboard


router = Router()


@router.message()
async def unknown_message(message: Message) -> None:
    await message.answer(
        "Я не совсем поняла сообщение. Выберите действие на клавиатуре или нажмите /start.",
        reply_markup=main_keyboard(),
    )

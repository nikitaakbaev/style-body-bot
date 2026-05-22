from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.main import main_keyboard


router = Router()

WELCOME_TEXT = (
    "Я помогу определить примерный тип фигуры по параметрам груди, талии и бедер, "
    "а затем подскажу, какие фасоны будут смотреться наиболее выигрышно."
)

HELP_TEXT = (
    "Для расчета нужны три параметра: обхват груди, талии и бедер.\n\n"
    "Грудь измеряется по самой объемной части. Талия — по самой узкой части живота. "
    "Бедра — по самой широкой части ягодиц. Вводите значения в сантиметрах.\n\n"
    "Тип фигуры определяется приблизительно, поэтому рекомендации лучше воспринимать "
    "как мягкую подсказку для выбора фасонов."
)


@router.message(CommandStart())
async def start_command(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(WELCOME_TEXT, reply_markup=main_keyboard())


@router.message(Command("help"))
@router.message(F.text == "Помощь")
async def help_command(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(HELP_TEXT, reply_markup=main_keyboard())


@router.message(F.text == "Главное меню")
async def main_menu(message: Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(WELCOME_TEXT, reply_markup=main_keyboard())

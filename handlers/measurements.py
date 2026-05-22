from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from database.db import upsert_user_profile
from keyboards.main import result_keyboard
from services.body_type_detector import detect_body_type
from services.recommendations import format_result_text
from utils.validators import parse_measurement


router = Router()

INVALID_MEASUREMENT_TEXT = (
    "Пожалуйста, введите число от 40 до 200 см. Можно использовать точку или запятую."
)


class MeasurementsForm(StatesGroup):
    bust = State()
    waist = State()
    hips = State()


@router.message(F.text.in_({"Определить тип фигуры", "Рассчитать заново"}))
async def start_measurements(message: Message, state: FSMContext) -> None:
    await state.clear()
    await state.set_state(MeasurementsForm.bust)
    await message.answer("Введите обхват груди в см")


@router.message(MeasurementsForm.bust)
async def process_bust(message: Message, state: FSMContext) -> None:
    bust = parse_measurement(message.text or "")
    if bust is None:
        await message.answer(INVALID_MEASUREMENT_TEXT)
        return

    await state.update_data(bust=bust)
    await state.set_state(MeasurementsForm.waist)
    await message.answer("Введите обхват талии в см")


@router.message(MeasurementsForm.waist)
async def process_waist(message: Message, state: FSMContext) -> None:
    waist = parse_measurement(message.text or "")
    if waist is None:
        await message.answer(INVALID_MEASUREMENT_TEXT)
        return

    await state.update_data(waist=waist)
    await state.set_state(MeasurementsForm.hips)
    await message.answer("Введите обхват бедер в см")


@router.message(MeasurementsForm.hips)
async def process_hips(message: Message, state: FSMContext) -> None:
    hips = parse_measurement(message.text or "")
    if hips is None:
        await message.answer(INVALID_MEASUREMENT_TEXT)
        return

    data = await state.get_data()
    bust = data["bust"]
    waist = data["waist"]
    detection = detect_body_type(bust=bust, waist=waist, hips=hips)

    if message.from_user is not None:
        await upsert_user_profile(
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            bust=bust,
            waist=waist,
            hips=hips,
            body_type=detection["type"],
        )

    await state.clear()
    await message.answer(format_result_text(detection), reply_markup=result_keyboard())

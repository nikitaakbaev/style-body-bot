from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Определить тип фигуры")],
            [KeyboardButton(text="Мой результат"), KeyboardButton(text="Помощь")],
        ],
        resize_keyboard=True,
    )


def result_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Рассчитать заново")],
            [KeyboardButton(text="Мой результат"), KeyboardButton(text="Главное меню")],
        ],
        resize_keyboard=True,
    )

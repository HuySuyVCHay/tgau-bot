from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_menu() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="ℹ️ О боте"))
    builder.add(KeyboardButton(text="📞 Контакты"))
    builder.add(KeyboardButton(text="Меню"))
    return builder.as_markup(resize_keyboard=True)
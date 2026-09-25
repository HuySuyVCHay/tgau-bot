from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def feedback_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="👍 Нравится", callback_data="like"))
    builder.add(InlineKeyboardButton(text="👎 Не нравится", callback_data="dislike"))
    return builder.as_markup()
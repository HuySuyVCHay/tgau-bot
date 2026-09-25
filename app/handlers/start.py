from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.keyboards.reply import main_menu

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Привет! Это команда /start 👋",
        reply_markup=main_menu()
    )
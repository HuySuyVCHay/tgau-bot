from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from app.keyboards.inline import feedback_keyboard

router = Router()


@router.message(F.text == "/menu")
async def show_menu(message: Message):
    await message.answer("Как тебе бот?", reply_markup=feedback_keyboard())


@router.callback_query(F.data == "like")
async def process_like(callback: CallbackQuery):
    await callback.answer("Спасибо! ❤️")
    await callback.message.edit_text("Ты выбрал: 👍")


@router.callback_query(F.data == "dislike")
async def process_dislike(callback: CallbackQuery):
    await callback.answer("Сейчас исправлю!")
    await callback.message.edit_text("Ты выбрал: 👎")


@router.message(F.text == "ℹ️ О боте")
async def about(message: Message):
    await message.answer("Это учебный бот на aiogram 3.x")


@router.message(F.text == "📞 Контакты")
async def contacts(message: Message):
    await message.answer("Связаться со мной: @твой_username")


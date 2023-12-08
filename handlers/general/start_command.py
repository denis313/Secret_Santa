from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from LEXICON.lexicon import LEXICON
from keyboards.general_keyboards import keyboard_start


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(text=LEXICON["start"], reply_markup=keyboard_start)

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from LEXICON.lexicon import LEXICON
from keyboards.general_keyboards import keyboard_start
from filters.filter import IsPrivate


router = Router()
router.message.filter(IsPrivate())


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(text=LEXICON["start"], reply_markup=keyboard_start)

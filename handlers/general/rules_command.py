from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from LEXICON.lexicon import LEXICON
from filters.filter import IsPrivate
from keyboards.general_keyboards import keyboard_start


router = Router()


@router.message(Command('rules'))
async def start(message: Message):
    await message.answer(LEXICON["rules"])

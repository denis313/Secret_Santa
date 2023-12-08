from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from LEXICON.lexicon import LEXICON

router = Router()


@router.message(Command('help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON['help'])

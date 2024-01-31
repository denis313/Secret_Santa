from aiogram import Router
from aiogram.fsm.state import default_state
from aiogram.types import Message
from aiogram.filters import Command, StateFilter

from LEXICON.lexicon import LEXICON
from filters.filter import IsPrivate

router = Router()


@router.message(StateFilter(default_state), IsPrivate())
async def other_text(message: Message):
    await message.answer(text="Я тебя не понимаю( Используй кнопки")

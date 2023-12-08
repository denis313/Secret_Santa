from aiogram import F, Router
from aiogram.types import CallbackQuery

from LEXICON.lexicon import LEXICON_Creator

router = Router()


@router.callback_query(F.data == 'creator')
async def new_creator(callback: CallbackQuery):
    await callback.answer(text=LEXICON_Creator["creator_start"])

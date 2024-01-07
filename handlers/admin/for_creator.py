from aiogram import F, Router
from aiogram.types import CallbackQuery
from LEXICON.lexicon import LEXICON_Creator, LEXICON_keyboard
from filters.filter import IsPrivate

router = Router()
router.message.filter(IsPrivate())


@router.callback_query(F.data == LEXICON_keyboard["keyboard_start_1"][1])
async def new_creator(callback: CallbackQuery):
    id_creator = callback.from_user.id
    await callback.message.edit_text(text=LEXICON_Creator["creator_start"])

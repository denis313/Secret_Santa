from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery

from filters.filter import IsPrivate
from LEXICON.lexicon import LEXICON_user
from keyboards.general_keyboards import questionnaire

router = Router()
router.message.filter(IsPrivate())


@router.callback_query(F.data == 'user')
async def for_new_user(callback: CallbackQuery):
    print(callback)
    user = callback.from_user
    if not user:
        await callback.message.edit_text(text=LEXICON_user["not_in_the_game"].format(name=user.first_name))
    else:
        await callback.message.edit_text(text=LEXICON_user["in_the_game"].format(name=user.first_name),
                                         reply_markup=questionnaire)

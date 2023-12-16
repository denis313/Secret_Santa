from aiogram import Router, F, Bot
from aiogram.types import Message


from filters.filter import IsPrivate, IsBot
from LEXICON.lexicon import LEXICON_user

router = Router()
router.message.filter(~IsPrivate())


@router.message(F.content_type == 'new_chat_members', ~IsBot())
async def new_chat(message: Message):
    id_new_user = message.from_user.id  # new id_user
    print(message.chat.id) # id_chat
    await message.answer(LEXICON_user["user_start"].format(name=message.from_user.first_name))

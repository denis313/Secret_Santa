from aiogram import Router, F
from aiogram.types import Message

from config_data.value_bot import bot
from filters.filter import IsPrivate, IsBot
from LEXICON.lexicon import LEXICON_Creator

router = Router()
router.message.filter(~IsPrivate())


@router.message(F.content_type == 'new_chat_members', IsBot())
async def new_chat(message: Message):
    chat_members = await bot.get_chat_administrators(message.chat.id)
    user_ids = [member.user.id for member in chat_members]  # id creator
    await bot.send_message(user_ids[0], LEXICON_Creator["new_chat"])

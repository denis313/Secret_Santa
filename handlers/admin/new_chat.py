from aiogram import Router, F, Bot
from aiogram.types import Message

# .
from filters.filter import IsPrivate, IsBot
from LEXICON.lexicon import LEXICON_Creator

router = Router()
router.message.filter(~IsPrivate())


@router.message(F.content_type == 'new_chat_members', IsBot())
async def new_chat(message: Message, bot: Bot):
    chat_members = await bot.get_chat_administrators(message.chat.id)
    for admin in chat_members:
        if admin.status == "creator":
            await bot.send_message(admin.user.id, LEXICON_Creator["new_chat"])

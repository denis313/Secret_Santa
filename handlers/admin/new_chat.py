from aiogram import Router, F, Bot
from aiogram.types import Message

from LEXICON.lexicon import LEXICON_Creator
from config_data.config import DATABASE_URL
from database.requests import DatabaseManager
from filters.filter import IsPrivate, IsBot

router = Router()
router.message.filter(~IsPrivate())
dsn = DATABASE_URL
db_manager = DatabaseManager(dsn)


# регистрируем администратора  __tableuser__
@router.message(F.content_type == 'new_chat_members', IsBot())
async def new_chat(message: Message, bot: Bot):
    chat_members = await bot.get_chat_administrators(message.chat.id)
    id_chat = message.chat.id
    for admin in chat_members:
        if admin.status == "creator":
            # добавляем user_id, id_chat, creator_id в __tableuser__
            user_data = {"user_id": admin.user.id, "chat_id": id_chat, "creator_id": admin.user.id}
            await db_manager.add_user(user_data)
            await bot.send_message(admin.user.id, LEXICON_Creator["new_chat"])


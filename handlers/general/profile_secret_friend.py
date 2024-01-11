from aiogram import F, Router, Bot
from aiogram.types import Message

from LEXICON.lexicon import LEXICON_keyboard, LEXICON
from config_data.config import DATABASE_URL
from database.requests import DatabaseManager
from filters.filter import IsPrivate

router = Router()
router.message.filter(IsPrivate())
dsn = DATABASE_URL
db_manager = DatabaseManager(dsn=dsn)


@router.message(F.text == LEXICON_keyboard["button"][4])
async def profile(message: Message, bot: Bot):
    id_user = message.from_user.id
    id_friend = await db_manager.get_user_by_id(user_id=id_user)
    data = await db_manager.get_questionnaire_by_id(id_friend.id_secret_friend)
    await profile(bot, data=data, id_user=id_friend.id_secret_friend, text='', keyboard=None)

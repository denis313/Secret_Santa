import logging

from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery, Message

from LEXICON.lexicon import LEXICON_Creator, LEXICON_keyboard
from config_data.config import DATABASE_URL
from database.requests import DatabaseManager
from filters.filter import IsPrivate, IsCreator
from handlers.general.message_profile import profile
from services.services import random_assignment

logger = logging.getLogger(__name__)
router = Router()
router.message.filter(IsPrivate())
dsn = DATABASE_URL
db_manager = DatabaseManager(dsn=dsn)


@router.message(F.text == LEXICON_keyboard["button"][1])
async def start_the_game(message: Message, bot: Bot):
    all_users = await db_manager.get_all_users()
    if len(all_users) > 1:
        if all_users[0][4] == 1:
            await message.answer(LEXICON_Creator["already_game"])
        else:
            logger.debug('Отладочная информация - НАЧАЛО ИГРЫ')
            for your_id, friend_id in random_assignment(all_users):
                user_data = await db_manager.get_questionnaire_by_id(user_id=friend_id)
                await db_manager.update_user(user_id=your_id, user_data={"id_secret_friend": friend_id, "game_status": 1})
                if user_data:
                    await bot.send_message(chat_id=your_id, text=LEXICON_Creator["start_game"])
                    await profile(bot, data=user_data, id_user=your_id, text='', keyboard=None)
    else:
        await message.answer('Мало игроков')

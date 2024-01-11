from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery, Message

from LEXICON.lexicon import LEXICON_Creator, LEXICON_keyboard, LEXICON
from config_data.config import DATABASE_URL
from database.requests import DatabaseManager
from filters.filter import IsPrivate
from handlers.general.message_profile import profile
from services.services import random_assignment

router = Router()
router.message.filter(IsPrivate())
dsn = DATABASE_URL
db_manager = DatabaseManager(dsn=dsn)


@router.callback_query(F.data == LEXICON_keyboard["keyboard_start_1"][1])
async def new_creator(callback: CallbackQuery):
    # id_creator = callback.from_user.id
    await callback.message.edit_text(text=LEXICON_Creator["creator_start"])


@router.message(F.text == LEXICON_keyboard["button"][1])  # сделать проверку статуса у creator запущена ли игра
async def start_the_game(message: Message, bot: Bot):
    all_users = await db_manager.get_all_users()
    for your_id, friend_id in random_assignment(all_users):
        print('Random users:', random_assignment(all_users))
        user_data = await db_manager.get_questionnaire_by_id(user_id=friend_id)
        await db_manager.update_user(user_id=your_id, user_data={"id_secret_friend": friend_id})
        if user_data:
            await bot.send_message(chat_id=your_id, text=LEXICON["start_game"])
            await profile(bot, data=user_data, id_user=your_id, text='', keyboard=None)
        else:
            continue

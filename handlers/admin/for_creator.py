from aiogram import F, Router, Bot
from aiogram.types import CallbackQuery, Message

from LEXICON.lexicon import LEXICON_Creator, LEXICON_keyboard, LEXICON
from config_data.config import DATABASE_URL
from database.requests import DatabaseManager
from filters.filter import IsPrivate
from services.services import random_assignment

router = Router()
router.message.filter(IsPrivate())
dsn = DATABASE_URL
db_manager = DatabaseManager(dsn=dsn)


@router.callback_query(F.data == LEXICON_keyboard["keyboard_start_1"][1])
async def new_creator(callback: CallbackQuery):
    # id_creator = callback.from_user.id
    await callback.message.edit_text(text=LEXICON_Creator["creator_start"])


@router.message(F.text == LEXICON_keyboard["button"][0])
async def start_the_game(message: Message, bot: Bot):
    all_users = await db_manager.get_all_users()
    for your_id, friend_id in random_assignment(all_users):
        print('Random users:', random_assignment(all_users))
        data = await db_manager.get_questionnaire_by_id(user_id=friend_id)
        if data:
            await bot.send_message(chat_id=your_id, text=LEXICON["start_game"])
            # await bot.send_photo(photo=data.photo, chat_id=your_id,
            #                      caption=LEXICON["profile"].format(name=data.name,
            #                                                        sex=data.sex,
            #                                                        clothing_brand=data.clothing_brand,
            #                                                        color_palette=data.color_palette,
            #                                                        sizes=data.sizes,
            #                                                        fashion_style=data.fashion_style,
            #                                                        hobby=data.hobby,
            #                                                        allergy=data.allergy,
            #                                                        salty_or_sweet=data.salty_or_sweet,
            #                                                        dream=data.dream))
        else:
            continue

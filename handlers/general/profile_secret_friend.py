from aiogram import F, Router, Bot
from aiogram.types import Message

from LEXICON.lexicon import LEXICON_keyboard, LEXICON_user, LEXICON
from config_data.config import DATABASE_URL
from database.requests import DatabaseManager
from filters.filter import IsPrivate
from handlers.general.message_profile import profile
from keyboards.general_keyboards import keyboard_friend, keyboard_user

router = Router()
router.message.filter(IsPrivate())
dsn = DATABASE_URL
db_manager = DatabaseManager(dsn=dsn)


@router.message(F.text == LEXICON_keyboard["button"][4])
async def secret_friend(message: Message):
    await message.answer(LEXICON_user["secret_friend"], reply_markup=keyboard_friend.as_markup(resize_keyboard=True))


@router.message(F.text == LEXICON_keyboard["friend_button"][0])
async def profile_secret_friend(message: Message, bot: Bot):
    id_user = message.from_user.id
    id_friend = await db_manager.get_user_by_id(user_id=id_user)
    data = await db_manager.get_questionnaire_by_id(id_friend.id_secret_friend)
    await profile(bot, data=data, id_user=id_user, text='', keyboard=None)


@router.message(F.text == LEXICON_keyboard["friend_button"][1])
async def gift_list_secret_friend(message: Message):
    id_user = message.from_user.id
    id_friend = await db_manager.get_user_by_id(user_id=id_user)
    data = await db_manager.get_gift_list(user_id=id_friend.id_secret_friend)
    print(data)
    if data.list == "СЮРПРИЗ":
        await message.answer(LEXICON["surprise"].format(gift_list=data.list))
    else:
        await message.answer(LEXICON_keyboard["gift_list_friend"].format(gift_list=data.list))


@router.message(F.text == LEXICON["menu"])
async def gift_list_secret_friend(message: Message):
    await message.answer('Хоу-хоу-хоу🎅', reply_markup=keyboard_user.as_markup(resize_keyboard=True))

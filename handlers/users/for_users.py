from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message, UserProfilePhotos

from LEXICON.lexicon import LEXICON_user, LEXICON_keyboard, LEXICON
from config_data.config import DATABASE_URL
from database.requests import DatabaseManager
from filters.filter import IsPrivate
from keyboards.general_keyboards import questionnaire, keyboard_change, keyboard_change_list, keyboard_new_list

router = Router()
router.message.filter(IsPrivate())
dsn = DATABASE_URL
db_manager = DatabaseManager(dsn=dsn)


@router.callback_query(F.data == LEXICON_keyboard["keyboard_start_2"][1])
async def for_new_user(callback: CallbackQuery):
    user = callback.from_user
    if await db_manager.get_user_by_id(user_id=user.id):
        await callback.message.edit_text(text=LEXICON_user["in_the_game"].format(name=user.first_name),
                                         reply_markup=questionnaire)
    else:
        await callback.message.edit_text(text=LEXICON_user["not_in_the_game"].format(name=user.first_name))


@router.message(F.text == LEXICON_keyboard["button"][0])
async def your_questionnaire(message: Message, bot: Bot):
    data = await db_manager.get_questionnaire_by_id(message.from_user.id)
    print('Profile - ', data)
    if data:
        await bot.send_photo(chat_id=message.from_user.id, photo=data.photo,
                             caption=LEXICON["profile"].format(name=data.name,
                                                               sex=data.sex,
                                                               clothing_brand=data.clothing_brand,
                                                               color_palette=data.color_palette,
                                                               sizes=data.sizes,
                                                               fashion_style=data.fashion_style,
                                                               hobby=data.hobby,
                                                               allergy=data.allergy,
                                                               salty_or_sweet=data.salty_or_sweet,
                                                               dream=data.dream),
                             reply_markup=keyboard_change)
    else:
        await message.answer(text=LEXICON_user["in_the_game"].format(name=message.from_user.first_name),
                             reply_markup=questionnaire)


@router.message(F.text == LEXICON_keyboard["button"][1])
async def gift_list(message: Message):
    data = await db_manager.get_gift_list(user_id=message.from_user.id)
    # print('Gift_list - ', data)
    if not data:
        await message.answer(LEXICON["list"], reply_markup=keyboard_new_list)
        # print('Create list')
    else:
        await message.answer(LEXICON["gift_list"].format(gift_list=data.list), reply_markup=keyboard_change_list)
        # print('Gift List')

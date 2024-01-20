from aiogram import F, Router, Bot
from aiogram.types import Message, CallbackQuery

from LEXICON.lexicon import LEXICON_keyboard, LEXICON_user, LEXICON
from config_data.config import DATABASE_URL
from database.requests import DatabaseManager
from filters.filter import IsPrivate
from handlers.general.message_profile import profile
from keyboards.callback_data_classes import CallbackFactory
from keyboards.general_keyboards import keyboard_friend, keyboard_user, keyboard_creator, keyboard_list
from services.parsing import read_json

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


@router.message(F.text == LEXICON_keyboard["friend_button"][2])
async def gift_list_secret_friend(message: Message):
    id_user = message.from_user.id
    id_friend = await db_manager.get_user_by_id(user_id=id_user)
    data = await db_manager.get_gift_list(user_id=id_friend.id_secret_friend)
    if data.list == "СЮРПРИЗ":
        await message.answer(LEXICON["surprise"].format(gift_list=data.list))
    else:
        await message.reply(LEXICON["gifts"], reply_markup=keyboard_list(user_id=id_friend.id_secret_friend,
                                                                         gifts=data.list))


@router.message(F.text == LEXICON["menu"])
async def gift_list_secret_friend(message: Message):
    if (await db_manager.get_user_by_id(user_id=message.from_user.id)).creator_id:
        await message.answer('Хоу-хоу-хоу🎅', reply_markup=keyboard_creator.as_markup(resize_keyboard=True))
    else:
        await message.answer('Хоу-хоу-хоу🎅', reply_markup=keyboard_user.as_markup(resize_keyboard=True))


@router.callback_query(CallbackFactory.filter())
async def gift_details(callback: CallbackQuery, callback_data: CallbackFactory):
    id_user = callback_data.user_id
    index = callback_data.index
    gift = (await db_manager.get_gift_list(user_id=id_user)).list.strip()
    data = read_json(user_id=id_user)
    # print(data[-1]['id'])
    await callback.message.edit_text(f"Подробности о подарке {gift}:\n"
                                  f"Дешевый вариант: \n" + LEXICON["general_list"].format(id=data[0]["id"],
                                                                                          brand=data[0]["brand"],
                                                                                          name=data[0]["name"],
                                                                                          price=data[0]["price"],
                                                                                          supplierRating=data[0][
                                                                                              "supplierRating"],
                                                                                          feedbacks=data[0][
                                                                                              "feedbacks"]) +
                                  f"\nДорогой вариант: \n" +
                                  LEXICON["general_list"].format(id=data[-1]["id"],
                                                                 brand=data[-1]["brand"],
                                                                 name=data[-1]["name"],
                                                                 price=data[-1]["price"],
                                                                 supplierRating=data[-1]["supplierRating"],
                                                                 feedbacks=data[-1]["feedbacks"]) +
                                  f"\nДоступен в магазинах: All")
    # message_text += f"Доступен в магазинах: {', '.join(gift['shops'])}")
    # message_text = f"Подробности о подарке {gift['name']}:\n"
    # message_text += f"Дешевый вариант: {gift['price']['дешевый']} рублей\n"
    # message_text += f"Дорогой вариант: {gift['price']['дорогой']} рублей\n"
    # message_text += f"Доступен в магазинах: {', '.join(gift['shops'])}"

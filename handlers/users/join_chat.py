from aiogram import Router, F
from aiogram.types import Message


from filters.filter import IsPrivate
from LEXICON.lexicon import LEXICON_user


router = Router()
router.message.filter(~IsPrivate())


@router.message(F.content_type == 'new_chat_members')
async def on_user_joined(message: Message):
    new_user = message.new_chat_members[0]  # object
    id_user = new_user.id  # insert id_user in database
    id_chat = message.chat.id  # check the database for compliance id_chat
    if True:
        await message.answer(LEXICON_user["user_start"].format(name=f'@{new_user.username}'))
    else:
        await message.answer(LEXICON_user["user_start"].format(name=new_user.first_name))

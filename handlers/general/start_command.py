from aiogram import Router, Bot, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from LEXICON.lexicon import LEXICON
from keyboards.general_keyboards import keyboard_start, read
from filters.filter import IsPrivate


router = Router()
router.message.filter(IsPrivate())


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(text=LEXICON["start"], reply_markup=keyboard_start)


@router.message(Command('rules'))
async def start(message: Message, bot: Bot):
    await message.answer(LEXICON["rules"], reply_markup=read)
    await bot.delete_message(message.chat.id, message.message_id)


@router.callback_query(F.data == 'read')
async def new_creator(callback: CallbackQuery):
    await callback.message.delete()

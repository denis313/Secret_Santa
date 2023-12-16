from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, BotCommand
from LEXICON.lexicon import LEXICON

btn_1 = InlineKeyboardButton(text='Создать игру', callback_data='creator')
btn_2 = InlineKeyboardButton(text='Вступить в игру', callback_data='user')
keyboard_start = InlineKeyboardMarkup(inline_keyboard=[[btn_1, btn_2]])

read = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Я прочитал', callback_data='read')]])

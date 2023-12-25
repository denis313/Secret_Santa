from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, BotCommand
from LEXICON.lexicon import LEXICON_keyboard

btn_1 = InlineKeyboardButton(text=LEXICON_keyboard["keyboard_start_1"][0],
                             callback_data=LEXICON_keyboard["keyboard_start_1"][1])
btn_2 = InlineKeyboardButton(text=LEXICON_keyboard["keyboard_start_2"][0],
                             callback_data=LEXICON_keyboard["keyboard_start_2"][1])
keyboard_start = InlineKeyboardMarkup(inline_keyboard=[[btn_1, btn_2]])

# keyboard for read rules
read = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=LEXICON_keyboard["read"][0],
                                                                   callback_data=LEXICON_keyboard["read"][1])]])

# keyboard for user questionnaire
questionnaire = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(
    text=LEXICON_keyboard["questionnaire"][0],
    callback_data=LEXICON_keyboard["questionnaire"][1])]])


next_questionnaire = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(
    text='Следующий вопрос',
    callback_data='next')]])

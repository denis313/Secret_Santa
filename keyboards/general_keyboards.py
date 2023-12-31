from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
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

# keyboard for sex
sex = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='М'),
                                     KeyboardButton(text='Ж')]],
                          resize_keyboard=True)

# keyboard for sizes
sizes = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='S'),
                                       KeyboardButton(text='M'),
                                       KeyboardButton(text='L'),
                                       KeyboardButton(text='XL')]],
                            resize_keyboard=True)

# keyboard for user
keyboard_user = (ReplyKeyboardBuilder())
keyboard_user.row(*[KeyboardButton(text=bt) for bt in LEXICON_keyboard["button"][1:]], width=2)

# keyboard for creator
keyboard_creator = (ReplyKeyboardBuilder())
keyboard_creator.row(*[KeyboardButton(text=bt) for bt in LEXICON_keyboard["button"]], width=1)

# keyboard for change questionnaire
keyboard_change = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(
    text=LEXICON_keyboard["change_b"][0],
    callback_data=LEXICON_keyboard["change_b"][1])]])

# keyboard for stop FSM
keyboard_stop_FSM = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=LEXICON_keyboard["stop"])]],
                                        resize_keyboard=True)

# keyboard for new list
keyboard_new_list = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(
    text=LEXICON_keyboard["new_list"][0],
    callback_data=LEXICON_keyboard["new_list"][1])]])

# keyboard for change list
keyboard_change_list = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(
    text=LEXICON_keyboard["change_l"][0],
    callback_data=LEXICON_keyboard["change_l"][1])]])

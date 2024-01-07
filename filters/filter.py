from aiogram.filters import Filter
from aiogram.types import Message


import re

from LEXICON.lexicon import LEXICON_keyboard


# delete characters in string
def keep_letters_and_spaces(input_string):
    # Используем регулярное выражение для удаления символов, кроме букв и пробелов
    cleaned_string = re.sub(r'[^a-zA-Z\s]', '', input_string)
    return cleaned_string


class IsPrivate(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.chat.type == 'private'


class IsBot(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.new_chat_members[0].is_bot


class IsAlpha(Filter):
    async def __call__(self, message: Message) -> bool:
        return all([i.isalpha() for i in keep_letters_and_spaces(message.text).split()])


class IsDigit(Filter):
    async def __call__(self, message: Message) -> bool:
        return all([i.isdigit() for i in message.text.split()])

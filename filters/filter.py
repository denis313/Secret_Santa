from aiogram.filters import BaseFilter
from aiogram.types import Message


import re


# delete characters in string
def keep_letters_and_spaces(input_string):
    # Используем регулярное выражение для удаления символов, кроме букв и пробелов
    cleaned_string = re.sub(r'[^a-zA-Z\s]', '', str(input_string))
    return cleaned_string


class IsPrivate(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.chat.type == 'private'


class IsBot(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return message.new_chat_members[0].is_bot


class IsAlpha(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return all([i.isalpha() for i in keep_letters_and_spaces(message.text).split()])


class IsDigit(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return all([i.isdigit() for i in message.text.split()])


class IsCreator(BaseFilter):
    def __init__(self, user_data):
        self.user_data = user_data

    async def __call__(self, user_data) -> bool:
        if user_data.creator_id:
            return user_data.creator_id
        else:
            return False

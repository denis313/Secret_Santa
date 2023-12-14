from aiogram.filters import Filter
from aiogram.types import Message


class IsPrivate(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.chat.type == 'private'


class IsBot(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.new_chat_members[0].is_bot

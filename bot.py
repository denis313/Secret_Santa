import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers.general import start_command, FSM_questionnaire, profile_secret_friend, help_command, rules_command
from handlers.admin import for_creator, new_chat
from handlers.users import join_chat, for_users

# Инициализируем логгер
logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота
async def main():
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Загружаем конфиг в переменную config
    config: Config = load_config()
    # Инициализируем бот и диспетчер
    dp = Dispatcher()
    bot = Bot(token=config.tg_bot.token,
              parse_mode='HTML')

    # Регистриуем роутеры в диспетчере
    dp.include_routers(start_command.router, help_command.router, rules_command.router, join_chat.router,
                       for_users.router,
                       FSM_questionnaire.router,
                       profile_secret_friend.router)
    dp.include_routers(for_creator.router,
                       new_chat.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("stopped")

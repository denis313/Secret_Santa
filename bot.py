import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers.general import start_command, help_command, rules_command
from handlers.admin import new_creator, new_chat


# Инициализируем логгер
logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота
async def main():
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')


    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    dp = Dispatcher()
    bot = Bot(token=config.tg_bot.token,
              parse_mode='HTML')

    # Регистриуем роутеры в диспетчере
    dp.include_router(start_command.router)
    dp.include_routers(rules_command.router)
    dp.include_router(help_command.router)
    dp.include_routers(new_creator.router,
                       new_chat.router)


    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')
    try:
        # Пропускаем накопившиеся апдейты и запускаем polling
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        logger.info("stopped")


if __name__ == '__main__':
    asyncio.run(main())

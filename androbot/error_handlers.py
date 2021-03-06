from aiogram import types as aiotypes
from loguru import logger

from androbot.errors import BaseAppError, ErrorExample
from androbot.main import dp


@dp.errors_handler(exception=BaseAppError)
async def handle_app_error(update: aiotypes.Update, exception: BaseAppError) -> bool:
    if isinstance(exception, ErrorExample):
        logger.error("Expected error occurred {}", type(exception))
    elif isinstance(exception, BaseAppError):
        logger.error("Unexpected error occurred {}", exception)
    await exception.message.answer(exception.response)
    return True

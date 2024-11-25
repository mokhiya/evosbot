from loader import bot, logger
from main.config import DEVS
from aiogram import Dispatcher


async def send_notification_to_devs(dispatcher: Dispatcher):
    """Send a notification to all developers when the bot starts."""
    try:
        for dev in DEVS:
            await bot.send_message(dev, "Bot started to work")
        logger.info(f"Notifications sent to {len(DEVS)} developers.")
    except Exception as e:
        logger.error(f"While sending info to devs: {e}")

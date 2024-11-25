from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from main import config

from main.database import database
from utils.notify_devs import send_notification_to_devs
from utils.set_bot_commands import set_default_commands

bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


async def on_startup(dispatcher):
    await database.connect()
    await set_default_commands(dispatcher)
    await send_notification_to_devs(dispatcher)


# On shutdown
async def on_shutdown(dispatcher):
    await database.disconnect()


if __name__ == '__main__':
    dp.start_polling(on_startup=on_startup, on_shutdown=on_shutdown)

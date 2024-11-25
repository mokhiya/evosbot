import logging

from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage

from main import config
from middleware.language import setup_middleware


bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

logging.basicConfig(
    level=logging.WARNING,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("bot.log", mode="a")
    ]
)
logger = logging.getLogger(__name__)

i18n = setup_middleware(dp)
_ = i18n.gettext

print("Loading loader")
print("Loaded middleware")
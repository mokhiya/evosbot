from aiogram import Router, types
from aiogram.filters import Text
from loader import _

router = Router()

@router.message(Text(text=["Contact ☎️", "Aloqa ☎️", "Связаться ☎️"]))
async def contact_handler(message: types.Message):
    text = _("📲 Call center: 1112 or (71) 203-00-00")
    await message.answer(text=text)
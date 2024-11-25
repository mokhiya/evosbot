from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove, ContentType

from keyboards.common import phone_number_share_keyboard
from keyboards.default.user import user_main_menu_keyboard, languages
from loader import _
from utils.db_commands.user import get_user, add_user
from utils.get_location import get_full_address

# Define router
router = Router()

# Define FSM States
class RegisterState(StatesGroup):
    language = State()
    full_name = State()
    phone_number = State()


@router.message(F.content_type == ContentType.LOCATION)
async def get_full_location(message: types.Message):
    address = await get_full_address(latitude=message.location.latitude, longitude=message.location.longitude)
    await message.answer(text=address)


@router.message(F.text == "/start")
async def start_handler(message: types.Message, state: FSMContext):
    await state.clear()
    user = await get_user(chat_id=message.chat.id)
    if user:
        text = f"Welcome back, {message.chat.first_name}!"
        await message.answer(text=text, reply_markup=await user_main_menu_keyboard())
    else:
        text = "Please select your language / Пожалуйста, выберите язык / Iltimos, til tanlang:"
        await message.answer(text=text, reply_markup=languages)
        await state.set_state(RegisterState.language)


@router.message(RegisterState.language)
async def language_handler(message: types.Message, state: FSMContext):
    language = message.text
    if language == "O'zbekcha 🇺🇿":
        language = "uz"
    elif language == "Русский 🇷🇺":
        language = "ru"
    else:
        language = "en"
    await state.update_data(language=language)
    text = _("Sorry, you have to enter your full name", locale=language)
    await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
    await state.set_state(RegisterState.full_name)


@router.message(RegisterState.full_name)
async def get_full_name_handler(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    data = await state.get_data()
    language = data.get('language')

    text = _("Please, enter your phone number by the button below 👇", locale=language)
    await message.answer(text=text, reply_markup=await phone_number_share_keyboard())
    await state.set_state(RegisterState.phone_number)


@router.message(RegisterState.phone_number, F.content_type == ContentType.CONTACT)
async def get_phone_number_handler(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    data = await state.get_data()
    language = data.get('language')

    new_user = await add_user(message=message, data=data)
    if new_user:
        text = _("You have successfully registered ✅", locale=language)
        await message.answer(text=text, reply_markup=await user_main_menu_keyboard())
    else:
        text = _("Sorry, please try again later 😔", locale=language)
        await message.answer(text=text)
    await state.clear()

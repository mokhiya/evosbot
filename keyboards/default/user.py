from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def user_main_menu_keyboard():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Menu")
            ],
            [
                KeyboardButton(text="My orders"),
            ],
            [
                KeyboardButton(text="Feedback"),
                KeyboardButton(text="Settings"),
            ]
        ], resize_keyboard=True
    )

    return markup

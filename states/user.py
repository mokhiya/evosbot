from aiogram.fsm.state import State, StatesGroup


class RegisterState(StatesGroup):
    """
    Represents the states of the user registration process.

    Attributes:
        language (State): State for choosing a language.
        full_name (State): State for entering the user's full name.
        phone_number (State): State for entering the phone number.
    """
    language = State()
    full_name = State()
    phone_number = State()

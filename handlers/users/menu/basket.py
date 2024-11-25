from aiogram import types

from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from loader import _
from utils.basket import get_user_basket

router = Router()


@router.message_handler(commands=['basket'])
async def view_basket(message: types.Message, state: FSMContext):
    user_basket = await get_user_basket(message.from_user.id)

    if user_basket:
        builder = InlineKeyboardBuilder()

        total_price = 0
        basket_details = ""

        for item in user_basket:
            meal_name = item['meal_name']
            quantity = item['quantity']
            price = item['price']
            meal_total = quantity * price

            basket_details += f"{meal_name} x{quantity} = ${meal_total}\n"
            total_price += meal_total

            builder.add(
                InlineKeyboardButton(
                    text=_(f"Remove {meal_name}"),
                    callback_data=f"remove_basket_{item['meal_id']}"
                )
            )

        builder.add(
            InlineKeyboardButton(
                text="Confirm Order",
                callback_data="confirm_order"
            )
        )

        basket_details += _(f"\nTotal Price: ${total_price}")

        await message.answer(basket_details, reply_markup=builder.as_markup())

    else:
        await message.answer("Your basket is empty. Please add some meals to it.")


@router.message_handler(commands=['basket'])
async def view_basket(message: types.Message, state: FSMContext):
    user_basket = await get_user_basket(message.from_user.id)

    if user_basket:
        builder = InlineKeyboardBuilder()

        total_price = 0
        basket_details = ""

        for item in user_basket:
            meal_name = item['meal_name']
            quantity = item['quantity']
            price = item['price']
            meal_total = quantity * price

            basket_details += f"{meal_name} x{quantity} = ${meal_total}\n"
            total_price += meal_total

            builder.add(
                InlineKeyboardButton(
                    text=f"Remove {meal_name}",
                    callback_data=f"remove_basket_{item['meal_id']}"
                )
            )

        builder.add(
            InlineKeyboardButton(
                text=_("Confirm Order"),
                callback_data="confirm_order"
            )
        )

        basket_details += _(f"\nTotal Price: ${total_price}")

        await message.answer(basket_details, reply_markup=builder.as_markup())
    else:
        await message.answer(_("Your basket is empty. Please add some meals to it."))

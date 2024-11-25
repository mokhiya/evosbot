from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton

from main import database
from aiogram import types, Router
from main.models import meals, orders
from utils.notify_devs import send_notification_to_devs

router = Router()
@router.callback_query_handler(lambda c: c.data == "confirm_order")
async def confirm_order(callback_query: types.CallbackQuery, state: FSMContext):
    # Retrieve the user's basket (in-memory or from a database)
    user_basket = await get_user_basket(callback_query.from_user.id)

    if user_basket:
        total_price = 0  # Initialize total price
        meal_ids = []  # List of meal ids for the order

        # Loop through the basket and calculate total price
        for item in user_basket:
            meal_id = item['meal_id']
            quantity = item['quantity']
            price = item['price']
            meal_total = quantity * price
            total_price += meal_total
            meal_ids.append(meal_id)

        # Insert order into the orders table
        order_query = orders.insert().values(
            user_id=callback_query.from_user.id,
            total_price=total_price,
            meal_ids=meal_ids,
        )
        order_id = await database.execute(order_query)

        # Send a confirmation message to the user
        await callback_query.message.answer(f"Your order has been placed! Total: ${total_price}. Thank you!")

        # Send a notification to admins or developers about the new order
        await send_notification_to_devs(callback_query.message, f"New order placed by user {callback_query.from_user.id}. Total: ${total_price}")

        # Clear the user's basket after confirming the order
        await clear_user_basket(callback_query.from_user.id)

    else:
        await callback_query.message.answer("Your basket is empty. Add some meals to your basket first.")

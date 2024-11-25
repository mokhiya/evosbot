from aiogram import types


async def set_default_commands(dp):
    """Set default bot commands"""
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Start using the bot 🚀️️️️️️"),
            types.BotCommand("help", "Find all features 🤖"),
            types.BotCommand("feedback", "Send feedback to admin 📝"),
        ]
    )

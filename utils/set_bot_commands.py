from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("info", "Вывести справку"),
            types.BotCommand("remove_me", "Видалити мене з бази даних"),
            types.BotCommand("howdoisay", "Перекладач"),
            types.BotCommand('test', 'Почати тест на визначення рівня англійської'),
            types.BotCommand("learn", "Learning")
        ]
    )

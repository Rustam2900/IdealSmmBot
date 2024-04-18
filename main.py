import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from config import TOKEN

dp = Dispatcher()


async def main() -> None:
    dp = Dispatcher()
    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    commands = [
        types.BotCommand(command="start", description="botga ishga tushurish uchun bosing")
    ]
    await bot.set_my_commands(commands)

    @dp.message(CommandStart())
    async def command_start_handler(message: Message):
        await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

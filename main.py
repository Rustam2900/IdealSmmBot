import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, Router, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import TOKEN
from AccountFilling import router as all_routers

router = Router()
router.include_router(all_routers)


async def main() -> None:
    dp = Dispatcher()
    bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    commands = [
        types.BotCommand(command="start", description="botga ishga tushurish uchun bosing")
    ]
    dp.include_router(router)
    await bot.set_my_commands(commands)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

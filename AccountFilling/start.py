from aiogram import Router, types, Bot
from aiogram.filters import CommandStart
from conustant import MAIN_TEXT
from AccountFilling.keyboard_kb import main_menu
# from databases.database import SMM, Session

router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message, bot: Bot):
    # user_id = message.from_user.id
    # first_name = message.from_user.first_name
    # created = message.date
    #
    # user = SMM(user_id=user_id, first_name=first_name, created=created)
    # session = Session()
    # session.add(user)
    # session.commit()
    await message.answer(text=MAIN_TEXT, reply_markup=main_menu())

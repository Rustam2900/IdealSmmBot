from aiogram import types
from aiogram import Router, F

from conustant import *

router = Router()


@router.message(F.text == SUPPORT)
async def lang_uz(message: types.Message):
    await message.answer(text=SUPPORT_TEXT, reply_markup=None
                         )

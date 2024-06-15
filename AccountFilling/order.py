from aiogram import types
from aiogram import Router, F

from conustant import *
from .keyboard_kb import main_menu_, lang

router = Router()


@router.message(F.contact)
async def nomer_(message: types.Message):
    await message.reply(text=f"Ro’yxatdan muvaffaqiyatli o’tdingiz  {message.from_user.first_name}",
                        reply_markup=main_menu_())


@router.message(F.text == UZ)
async def lang_uz(message: types.Message):
    await message.answer(text=MAIN_TEXT, reply_markup=lang())


@router.message(F.text == RU)
async def lang_uz(message: types.Message):
    await message.answer(text=MAIN_TEXT, reply_markup=lang())


@router.message(F.text == EN)
async def lang_uz(message: types.Message):
    await message.answer(text=MAIN_TEXT, reply_markup=lang())

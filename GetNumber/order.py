from aiogram import Router, F

from AccountFilling.keyboard_kb import lang
from GetNumber.inlayn_kb import main_nomer
from conustant import *
from aiogram import types

router = Router()


@router.message(F.text == GET_NUMBER)
async def lang_uz(message: types.Message):
    await message.answer(text=GET_NUMBER_TEXT, reply_markup=main_nomer())


@router.message(F.text == CANCEL)
async def cancel_(message: types.Message):
    await message.answer(text='.', reply_markup=lang())

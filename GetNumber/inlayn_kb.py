from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from conustant import I_AGREE, CANCEL


def main_nomer():
    buttons = [
        [KeyboardButton(text=I_AGREE, callback_data="agree"),
         KeyboardButton(text=CANCEL, callback_data="cancel")]
    ]

    keyboard = ReplyKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

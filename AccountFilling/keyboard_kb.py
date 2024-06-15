from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import KeyboardButton
from conustant import NOMER_, UZ, RU, EN, GET_NUMBER, SERVICES, ORDER, REFERRAL, MYACCOUNT, ACCOUNTFILLING, GUIDE, \
    SUPPORT


def main_menu():
    kb = [
        [KeyboardButton(text=NOMER_, request_contact=True)],
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def main_menu_():
    kb = [
        [KeyboardButton(text=UZ),
         KeyboardButton(text=RU),
         KeyboardButton(text=EN),
         ],

    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard


def lang():
    kb = [
        [KeyboardButton(text=GET_NUMBER)],
        [
            KeyboardButton(text=SERVICES),
            KeyboardButton(text=ORDER),
            KeyboardButton(text=REFERRAL),
        ],
        [
            KeyboardButton(text=MYACCOUNT),
            KeyboardButton(text=ACCOUNTFILLING),
            KeyboardButton(text=GUIDE),
            KeyboardButton(text=SUPPORT)
        ]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    return keyboard

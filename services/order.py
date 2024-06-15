import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import CallbackQuery
from referal import TOKEN, TEXT

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn = types.KeyboardButton('Xizmatlar')
    itembtn1 = types.KeyboardButton("To'lov")
    markup.add(itembtn, itembtn1)
    await message.answer("Xizmatlardan birini tanlang:", reply_markup=markup)


@dp.message_handler(lambda message: message.text == 'Xizmatlar')
async def xizmatlar(message: types.Message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    telegram_btn = types.InlineKeyboardButton('🔵 Telegram', callback_data='telegram')
    instagram_btn = types.InlineKeyboardButton('🔴 Instagram', callback_data='instagram')
    youtube_btn = types.InlineKeyboardButton('🟢 Youtube', callback_data='youtube')
    tiktok_btn = types.InlineKeyboardButton('⚫️ TikTok', callback_data='tiktok')
    markup.add(telegram_btn, instagram_btn, youtube_btn, tiktok_btn)
    await message.answer(
        "✅ Bizning xizmatlarimizni tanlaganingizdan xursandmiz! Quydagi Ijtimoiy tarmoqlardan birini tanlang.",
        reply_markup=markup)


@dp.callback_query_handler(lambda call: call.data == 'telegram')
async def telegram_buttons(call: types.CallbackQuery):
    markup = types.InlineKeyboardMarkup()
    ulanishlar_btn = types.InlineKeyboardButton('↪️ Ulanishlar', callback_data='ulanishlar')
    storislar_btn = types.InlineKeyboardButton('📖 Istoriya ko\'rish', callback_data='Istoriya kolar')
    guruhlar_btn = types.InlineKeyboardButton('⭐️ Premium 👤 Obunachilar', callback_data='guruhlar')
    boost_btn = types.InlineKeyboardButton('🔉 BOOST hikoyalar ovoz', callback_data='boost')
    avto_btn = types.InlineKeyboardButton('⏰ Avto ko\'rish', callback_data='avto')
    korish_btn = types.InlineKeyboardButton('👁 Ko\'rish', callback_data='korish')
    obunachi_btn = types.InlineKeyboardButton('👤 Obunachi', callback_data='obunachi')
    reaksiya_btn = types.InlineKeyboardButton('👍👎 Reaksiya', callback_data='reaksiya')
    premreak_btn = types.InlineKeyboardButton("Premium reaksiya", callback_data='premreak')
    ovoz_btn = types.InlineKeyboardButton("📊 Ovoz | So'rovnoma", callback_data='ovoz')

    markup.add(ulanishlar_btn, storislar_btn, guruhlar_btn, boost_btn, avto_btn, korish_btn, obunachi_btn, reaksiya_btn,
               premreak_btn, ovoz_btn)
    await call.message.answer("Telegram bo'limlaridan birini tanlang!", reply_markup=markup)


@dp.callback_query_handler(lambda call: call.data == 'instagram')
async def insta_buttons(call: types.CallbackQuery):
    markup = types.InlineKeyboardMarkup()
    video = types.InlineKeyboardButton('🎥 Video ko\'rish', callback_data='video')
    istoriy = types.InlineKeyboardButton('Istoriya ko\'rish', callback_data='istoriya')
    like = types.InlineKeyboardButton('🩷 Like', callback_data='like')
    oxvat = types.InlineKeyboardButton('Охваты', callback_data='oxvat')
    kafolat = types.InlineKeyboardButton('👤 Obunachi(♻️Kafolatlangan)', callback_data='kafolat')
    no_kafolat = types.InlineKeyboardButton('👤Obunachi(❌Kafolatlanmagan)', callback_data='no_kafolat')
    markup.add(video, kafolat, no_kafolat, istoriy, like, oxvat)
    await call.message.answer("Telegram bo'limlaridan birini tanlang!", reply_markup=markup)


@dp.callback_query_handler(lambda call: call.data == 'youtube')
async def insta_buttons(call: types.CallbackQuery):
    markup = types.InlineKeyboardMarkup()
    video = types.InlineKeyboardButton('🎥 Video ko\'rish', callback_data='video')
    like = types.InlineKeyboardButton('👍👎 Like', callback_data='like')
    shorts = types.InlineKeyboardButton('🔴 SHORTS ko\'rish', callback_data='shorts')
    komment = types.InlineKeyboardButton("Komentriya", callback_data='comment')

    markup.add(video, shorts, komment, like, )
    await call.message.answer("Telegram bo'limlaridan birini tanlang!", reply_markup=markup)


@dp.message_handler(lambda message: message.text == "To'lov")
async def xizmatlar(message: types.Message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    payme = types.InlineKeyboardButton("🔹Payme", callback_data='payme')
    click = types.InlineKeyboardButton('🔸Click', callback_data='click')
    appelsin = types.InlineKeyboardButton('🍊Appelsin', callback_data='appelsin')
    qivi = types.InlineKeyboardButton('🥝 Qivi', callback_data='qivi')
    payeer = types.InlineKeyboardButton('🅿️ Payeer', callback_data='payeer')
    cardlink = types.InlineKeyboardButton('💳 Cardlink', callback_data='cardlink')
    admin = types.InlineKeyboardButton('📲 Adminga murojat', url='https://admin')
    markup.add(payme, click, appelsin, qivi, payeer, cardlink)
    await message.answer(TEXT, reply_markup=markup)


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'payme')
async def payme_callback(callback_query: CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id,
                           "Balansizni necha so'mga to'ldirmoqchisiz?\nMinimal miqdor: 1000 so'm")
    amount_message = await bot.wait_for('message')
    try:
        amount = float(amount_message.text)
    except ValueError:
        await bot.send_message(callback_query.from_user.id, "Summani raqam ko'rinishida kiriting.")
        return
    payment_message = f"🔷 Payme to'lov tizimi orqali hisobni to'ldirish\n💳 To'lov miqdori: {amount:.2f} so'm"
    await bot.send_message(callback_query.from_user.id, payment_message)
    await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

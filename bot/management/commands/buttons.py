from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

start = ReplyKeyboardMarkup([
    [KeyboardButton('🚚 Yetkazib berish')],
    [KeyboardButton('📦 Buyurtma berish')],
    [KeyboardButton('🐣 Yetkazib erish')],
    [KeyboardButton('✍️ Taklif va shikoyatlar')],
], resize_keyboard=True)

phone = ReplyKeyboardMarkup([
    [KeyboardButton('📞 Send', request_contact=True)]
], resize_keyboard=True)
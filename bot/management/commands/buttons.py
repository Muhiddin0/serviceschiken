from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

start = ReplyKeyboardMarkup([
    [KeyboardButton('📦 Buyurtma berish')],
    [KeyboardButton('🚚 Yetkazib berish')],
    [KeyboardButton('🐣 Veterenariya ')],
    [KeyboardButton('✍️ Taklif va shikoyatlar')],
], resize_keyboard=True)
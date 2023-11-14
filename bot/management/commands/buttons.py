from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

start = ReplyKeyboardMarkup([
    [KeyboardButton('📦 Buyurtma berish')],
    [KeyboardButton('🚚 Yetkazib berish')],
    [KeyboardButton('🐣 Veterenariya ')],
    [KeyboardButton('✍️ Taklif va shikoyatlar')],
], resize_keyboard=True)

phone = ReplyKeyboardMarkup([
    [KeyboardButton('📞 Send', request_contact=True)]
], resize_keyboard=True)


location = ReplyKeyboardMarkup([
   [KeyboardButton("📍location", request_location=True)]], resize_keyboard=True)

register = ReplyKeyboardMarkup([
    [KeyboardButton("👨‍💻 Ro'yxatdan o'tish")]
], resize_keyboard=True)
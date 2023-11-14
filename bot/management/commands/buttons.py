from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

start = ReplyKeyboardMarkup([
    [KeyboardButton('📦 Buyurtma berish')],
    [KeyboardButton('🚚 Yetkazib berish')],
    [KeyboardButton('🐣 Veterenariya ')],
    [KeyboardButton('✍️ Taklif va shikoyatlar')],
], resize_keyboard=True)

phone = ReplyKeyboardMarkup([
    [KeyboardButton('📞 Send', request_contact=True)]
], resize_keyboard=True)
feedback = ReplyKeyboardMarkup([
    [KeyboardButton("🖌Taklif bildirish")],
    [KeyboardButton("🖍shikoyat bildirish")]
], resize_keyboard=True)
 



location = ReplyKeyboardMarkup([
   [KeyboardButton("📍location", request_location=True)]], resize_keyboard=True)

register = ReplyKeyboardMarkup([
    [KeyboardButton("👨‍💻 Ro'yxatdan o'tish")],
    [KeyboardButton("🔙 Orqaga")]
], resize_keyboard=True)

cancel = InlineKeyboardMarkup(row_width=1, inline_keyboard=[[InlineKeyboardButton('❌ Bekor qilish', callback_data='cancel')]])


remove_keyboard = ReplyKeyboardRemove()
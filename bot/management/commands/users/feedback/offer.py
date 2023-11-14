from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import User
from ...loader import dp, bot
from ... import texts, buttons
from ...states import Feedback

from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, \
    CallbackQuery

import requests

from aiogram.types import InlineKeyboardMarkup

import asyncio

admins = [
    5303925509
]



channels = [
    {
        "url":"https://t.me/testbotuchunnds",
        "id": "-1002010648507",
        "name":"chjannel",

    }
]


def is_admin(func):
    def decorator(msg):
        if msg.chat.id in admins:
            return func(msg)
        else:
            return

    return decorator
def is_channel(func):
    async def decerator(msg):
        left_channels = []
        for channel in channels:
            res=(await bot.get_chat_member(chat_id=channel["id"],user_id=msg.from_user.id)).status
            if res in ['administrator','creator','member']:
                continue
            else:
                left_channels.append(channel)
        if len(left_channels) >0:
            keywords =InlineKeyboardMarkup()
            for left_channel in left_channels:
                keywords.add(InlineKeyboardButton(text=left_channel['name'], url=left_channel['url']))

            keywords.add(InlineKeyboardButton(text="Tekshirish ☑️", callback_data="confirm"))
            try:
                await msg.answer("kanalga obuna boling",reply_markup=keywords)
            except Exception as e:
                print(e)
                await msg.answer("kanalga obuna boling")
        else:
            return await func(msg)
    return decerator



async def set_order_task(message: types.Message, state: FSMContext=None):
    await message.answer(text=texts.complaint_text)
    await Feedback.text.set()
    
    
@dp.message_handler(text='🖌Taklif bildirish', content_types='text')
@is_channel
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_order_task(message, state))





@dp.callback_query_handler(lambda msg: msg.data=="confirm")
@is_channel
async def confirm_handler(msg:CallbackQuery):
    await bot.delete_message(msg.from_user.id, message_id=msg.message.message_id)
    await msg.answer(text=texts.complaint_text)
    await Feedback.text.set()
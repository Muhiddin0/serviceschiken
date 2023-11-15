from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import User
from ...loader import dp, bot
from ... import texts, buttons
from ...states import Feedback

import asyncio

async def set_order_task(message: types.Message, state: FSMContext=None):
    await message.answer(text=texts.feed_text, reply_markup=buttons.feedback)
    await Feedback.text.set()
    
    
@dp.message_handler(text='✍️ Taklif va shikoyatlar', content_types='text')
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_order_task(message, state))





from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import User
from ...loader import dp, bot
from ... import texts, buttons
from ...states import DeliveryState

import asyncio

async def set_deliver_task(message: types.Message, state: FSMContext=None):
     await message.answer(text=texts.del_name)
     await DeliveryState.name.set()
    
    
@dp.message_handler(text='🚚 Yetkazib berish', content_types='text')
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_deliver_task(message, state))
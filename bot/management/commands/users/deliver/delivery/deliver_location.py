from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import User
from ....loader import dp, bot
from .... import texts, buttons
from ....states import DeliveryState

import asyncio

async def set_phone_task(message: types.Message, state: FSMContext=None):
    location = message.text

    state_data = await state.get_data()
    state_data['location'] = location

    await state.set_data(state_data)

    await message.answer(texts.deliver_price)
    
    await DeliveryState.price.set()
    
@dp.message_handler(content_types=types.ContentType.LOCATION, state=DeliveryState.location)
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_phone_task(message, state))
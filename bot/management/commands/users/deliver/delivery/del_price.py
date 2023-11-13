from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import User
from ....loader import dp, bot
from .... import texts, buttons
from ....states import DeliveryState

import asyncio

async def set_name_task(message: types.Message, state: FSMContext=None):
    price = message.text

    state_data = await state.get_data()
    state_data['price'] = price

    await state.set_data(state_data)

    await message.answer(texts.del_img)
    
    await DeliveryState.location.set()
    
    
@dp.message_handler(content_types='text', state=DeliveryState.price)
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_name_task(message, state))
from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import User
from ...loader import dp, bot
from ... import texts, buttons
from ...states import OrderState

import asyncio

async def set_name_task(message: types.Message, state: FSMContext=None):
    day = message.text

    state_data = await state.get_data()
    state_data['day'] = day

    await state.set_data(state_data)

    await message.answer(texts.set_price)
    
    await OrderState.price.set()
    
    
@dp.message_handler(content_types='text', state=OrderState.day)
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_name_task(message, state))
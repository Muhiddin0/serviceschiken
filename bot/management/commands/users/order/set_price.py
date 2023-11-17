from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import User
from ...loader import dp, bot
from ... import texts, buttons
from ...states import OrderState

import asyncio

async def set_name_task(message: types.Message, state: FSMContext=None):
    price = message.text

    if not price.isdigit():
        await message.answer(texts.price_error)
        return

    state_data = await state.get_data()
    state_data['price'] = price

    await state.set_data(state_data)

    await message.answer(texts.set_location, reply_markup=buttons.cancel)
    
    await OrderState.location.set()
    
    
@dp.message_handler(content_types='text', state=OrderState.price)
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_name_task(message, state))
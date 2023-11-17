from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import User
from ....loader import dp, bot
from .... import texts, buttons
from ....states import DeliveryState

import asyncio

async def set_phone_task(message: types.Message, state: FSMContext=None):
    phone = message.text

    if not phone.replace('+', '').isdigit():
        await message.answer(texts.phone_error)
        return
    
    state_data = await state.get_data()
    state_data['phone'] = phone

    await state.set_data(state_data)

    await message.answer(text=texts.great, reply_markup=buttons.location)
    await message.answer(text=texts.deliver_location, reply_markup=buttons.cancel)
    
    await DeliveryState.location.set()
    
    
@dp.message_handler(content_types='text', state=DeliveryState.phone)
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_phone_task(message, state))
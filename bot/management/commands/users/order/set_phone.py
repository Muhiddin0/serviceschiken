from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import User
from ...loader import dp, bot
from ... import texts, buttons
from ...states import OrderState

import asyncio

async def set_phone_task(message: types.Message, state: FSMContext=None):
    phone = message.contact.phone_number

    state_data = await state.get_data()
    state_data['phone'] = phone

    await state.set_data(state_data)

    await message.answer(text=texts.set_day, reply_markup=buttons.cancel)    
    
    await OrderState.day.set()
    
    
@dp.message_handler(content_types=types.ContentType.CONTACT, state=OrderState.phone)
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_phone_task(message, state))
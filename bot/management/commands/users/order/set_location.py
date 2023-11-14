import os
from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import User
from ...loader import dp, bot
from ... import texts, buttons
from ...states import OrderState

import asyncio

import dotenv

dotenv.load_dotenv()

async def set_phone_task(message: types.Message, state: FSMContext=None):
    location = message.text

    state_data = await state.get_data()
    state_data['location'] = location

    await state.set_data(state_data)

    await message.answer(text=texts.finish)    
    
    data = await state.get_data()

    await bot.send_message(
        chat_id=os.getenv('GROUP_CHAT_ID'),
        text=texts.send_order.format(data['name'],data['phone'], data['day'], data['price'], data['location'])
    )
    await state.finish()
    
    
@dp.message_handler(content_types=['text'], state=OrderState.location)
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_phone_task(message, state))
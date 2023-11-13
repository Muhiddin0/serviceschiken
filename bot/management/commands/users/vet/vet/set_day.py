from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import User
from ....loader import dp, bot
from .... import texts, buttons
from ....states import VetClientState

import asyncio

async def set_name_task(message: types.Message, state: FSMContext=None):
    day = message.text

    state_data = await state.get_data()
    state_data['day'] = day

    await state.set_data(state_data)

    await message.answer(texts.vet_humidity)
    
    await VetClientState.humidity.set()
    # set_humidity.py
    
@dp.message_handler(content_types='text', state=VetClientState.day)
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_name_task(message, state))
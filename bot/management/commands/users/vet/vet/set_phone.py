from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import User
from ....loader import dp, bot
from .... import texts, buttons
from ....states import VetClientState

import asyncio

async def set_phone_task(message: types.Message, state: FSMContext=None):
    phone = message.text

    state_data = await state.get_data()
    state_data['phone'] = phone

    await state.set_data(state_data)

    await message.answer(text=texts.vet_client_location)   
    
    await VetClientState.location.set()
    
    
@dp.message_handler(content_types=['text'], state=VetClientState.phone)
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_phone_task(message, state))
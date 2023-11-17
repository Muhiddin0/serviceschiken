from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import User
from ....loader import dp, bot
from .... import texts, buttons
from ....states import VetClientState

import asyncio

async def set_name_task(message: types.Message, state: FSMContext=None):
    temperature = message.text
    
    if not temperature.isdigit():
            await message.answer(texts.temperature_error)
            return
            
    state_data = await state.get_data()
    state_data['temperature'] = temperature

    await state.set_data(state_data)

    await message.answer(texts.vet_sickness, reply_markup=buttons.cancel)
    
    await VetClientState.sickness.set()

    
@dp.message_handler(content_types='text', state=VetClientState.temperature)
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_name_task(message, state))
from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import User
from ....loader import dp, bot
from .... import texts, buttons
from ....states import VetClientState

import asyncio

async def set_name_task(message: types.Message, state: FSMContext=None):
    sickness = message.text

    state_data = await state.get_data()
    state_data['sickness'] = sickness

    await state.set_data(state_data)

    await message.answer(texts.vet_diagnose, reply_markup=buttons.cancel)
    
    await VetClientState.diagnose.set()

    
@dp.message_handler(content_types='text', state=VetClientState.sickness)
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_name_task(message, state))
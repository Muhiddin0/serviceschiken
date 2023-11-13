from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import User
from ....loader import dp, bot
from .... import texts, buttons
from ....states import DeliveryState

import asyncio

async def set_name_task(message: types.Message, state: FSMContext=None):
    image = message.photo

    state_data = await state.get_data()
    state_data['image'] = image

    await state.set_data(state_data)

    await message.answer(texts.del_comment)
    
    await DeliveryState.location.set()
    
    
@dp.message_handler(content_types='text', state=DeliveryState.image)
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_name_task(message, state))
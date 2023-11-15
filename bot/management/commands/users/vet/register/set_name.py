from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import User
from ....loader import dp, bot
from .... import texts, buttons
from ....states import VetRegister

import asyncio

async def set_name_task(message: types.Message, state: FSMContext=None):
    name = message.text

    await state.set_data(
        {
            "name":name
        }
    )
    await message.answer(text=texts.great, reply_markup=buttons.phone)
    await message.answer(text=texts.set_phone, reply_markup=buttons.cancel)
    
    await VetRegister.phone.set()
    
    
@dp.message_handler(content_types='text', state=VetRegister.name)
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_name_task(message, state))
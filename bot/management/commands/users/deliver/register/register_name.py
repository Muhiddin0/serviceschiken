from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import User
from ....loader import dp, bot
from .... import texts, buttons
from ....states import SupplierRegisterState

import asyncio

async def set_name_task(message: types.Message, state: FSMContext=None):
    name = message.text
    await state.set_data(
        {
            "name":name
        }
    )
    await message.answer(text=texts.register_phone, reply_markup=buttons.phone)
    
    await SupplierRegisterState.phone.set()
    
    
@dp.message_handler(content_types='text', state=SupplierRegisterState.name)
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_name_task(message, state))
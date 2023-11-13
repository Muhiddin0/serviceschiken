from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import User
from ....loader import dp, bot
from .... import texts, buttons
from ....states import VetRegister

import asyncio

async def set_order_task(message: types.Message, state: FSMContext=None):
    await message.answer(text=texts.set_name)
    await VetRegister.name.set()
    
    
@dp.message_handler(text="👨‍💻 Ro'yxatdan o'tish", content_types='text')
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_order_task(message, state))
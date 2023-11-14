from aiogram import types
from aiogram.dispatcher import FSMContext

from ..loader import dp
from .. import texts, buttons

import asyncio

async def task(message: types.Message, state: FSMContext=None):
    await state.finish()
    await message.answer(texts.menu, reply_markup=buttons.start)
    
    
@dp.message_handler(state="*", content_types='text', text=['🔙 Orqaga'])
async def send_welcome(message: types.Message, state: FSMContext=None):
    asyncio.create_task(task(message, state))

# py manage.py startapp deliver
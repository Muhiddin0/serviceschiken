from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import User
from ..loader import dp, bot
from .. import texts, buttons

import asyncio

async def task(callbac_data: types.Message, state: FSMContext=None):
    await state.finish()
    await callbac_data.message.answer(texts.menu, reply_markup=buttons.start)
    
    
@dp.callback_query_handler(state="*", text_contains="cancel")
async def send_welcome(callbac_data: types.Message, state: FSMContext=None):
    asyncio.create_task(task(callbac_data, state))
import os
from aiogram import types
from aiogram.dispatcher import FSMContext

from ..loader import dp, bot
from .. import texts, buttons

import asyncio

async def check_deliver_task(callbac_data: types.CallbackQuery, state: FSMContext = None):
    user_id = callbac_data['from']['id']
    channel_chat_id = os.getenv('MAIN_GROUP_ID')
    user_status  = await bot.get_chat_member(chat_id=channel_chat_id, user_id=user_id)

    if user_status['status'] == 'left':
        await callbac_data.message.answer(texts.not_subscribe, reply_markup=buttons.chanel)
        return
    
    await callbac_data.message.answer(text=texts.feed_text, reply_markup=buttons.feedback)

@dp.callback_query_handler(state='*', text_contains="sub")
async def func(message: types.Message, state: FSMContext = None):
    asyncio.create_task(check_deliver_task(message, state))
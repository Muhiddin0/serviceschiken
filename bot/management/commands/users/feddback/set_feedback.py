from aiogram import types
from aiogram.dispatcher import FSMContext

from ...loader import dp, bot
from ... import texts, buttons

from dotenv import load_dotenv
import asyncio
import os

load_dotenv()


async def start_task(message: types.Message, state: FSMContext=None):
    user_id = message.from_user.id
    main_group_id = os.getenv("MAIN_GROUP_ID")
    user_status = await bot.get_chat_member(chat_id=main_group_id, user_id=user_id)

    if user_status['status'] == 'left':
        await message.answer(texts.not_subscribe, reply_markup=buttons.chanel)
        return

    await message.answer(texts.feed_text, reply_markup=buttons.feedback)
    
    
    
@dp.message_handler(state="*", content_types='text', text='✍️ Taklif va shikoyatlar')
async def send_welcome(message: types.Message, state: FSMContext=None):
    asyncio.create_task(start_task(message, state))
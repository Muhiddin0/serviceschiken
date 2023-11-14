import os
from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import User
from ...loader import dp, bot
from ... import texts, buttons
from ...states import Feedback

import asyncio

import dotenv

dotenv.load_dotenv()


async def set_name_task(message: types.Message, state: FSMContext=None):
    text = message.text
    await state.set_data(
        {
            "text":text
        }
    )
    # data = await state.get_data()
    # await bot.send_message(
    #     chat_id=os.getenv('GROUP_CHAT_ID'),
    #     text=texts.send_offer.format(data['text']),
    #     reply_markup=buttons.start
    # )

    await message.answer(text=texts.feedback_finish)
    
    await state.finish()
    
    
@dp.message_handler(content_types='text', state=Feedback.text)
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_name_task(message, state))


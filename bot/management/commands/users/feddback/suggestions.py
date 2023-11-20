from aiogram import types
from aiogram.dispatcher import FSMContext

from ...loader import dp, bot
from ... import texts, buttons
from ...states import Feedback

from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

async def start_task(message: types.Message, state: FSMContext=None):
    text = message.text
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    feddback_group = os.getenv('FEDDBACK_GROUP')

    await message.answer(text=texts.succes_feddback, reply_markup=buttons.start)

    await bot.send_message(
        chat_id=feddback_group,
        text=texts.feddback_caption.format(
            "Taklif",
            user_id,
            first_name,
            text
        )
    )
    await state.finish()
    
@dp.message_handler(state=Feedback.suggest, content_types='text',)
async def send_welcome(message: types.Message, state: FSMContext=None):
    asyncio.create_task(start_task(message, state))
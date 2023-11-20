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
    await message.answer(texts.great, reply_markup=buttons.remove_keyboard)
    await message.answer(texts.set_suggest, reply_markup=buttons.cancel)
    await Feedback.suggest.set()
    
@dp.message_handler(state="*", content_types='text', text='📃Taklif bildirish')
async def send_welcome(message: types.Message, state: FSMContext=None):
    asyncio.create_task(start_task(message, state))
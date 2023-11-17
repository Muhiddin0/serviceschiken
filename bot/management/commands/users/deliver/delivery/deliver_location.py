from aiogram import types
from aiogram.dispatcher import FSMContext
import requests

from bot.models import User
from ....loader import dp, bot
from .... import texts, buttons
from ....states import DeliveryState

import asyncio

async def set_phone_task(message: types.Message, state: FSMContext=None):
    lat = message.location.latitude
    lon = message.location.longitude

    YOUR_PRIVATE_TOKEN = "pk.ac43a63445fbb2ab91a912edbae60a24"
    url = f"https://us1.locationiq.com/v1/reverse.php?key={YOUR_PRIVATE_TOKEN}&lat={lat}&lon={lon}&format=json"
    response = requests.get(url).json()
    

    state_data = await state.get_data()
    state_data['location'] = response['display_name']

    await state.set_data(state_data)

    await message.answer(texts.deliver_price, reply_markup=buttons.cancel)
    
    await DeliveryState.price.set()
    
@dp.message_handler(content_types=types.ContentType.LOCATION, state=DeliveryState.location)
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_phone_task(message, state))
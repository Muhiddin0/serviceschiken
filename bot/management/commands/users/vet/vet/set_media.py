from django.core.files.images import ImageFile

import io
from aiogram import types
from aiogram.dispatcher import FSMContext
import requests

from ....loader import dp, bot
from .... import texts, buttons
from ....states import VetClientState
from vet.models import VetClient

import asyncio
from asgiref.sync import sync_to_async


import dotenv
import os

dotenv.load_dotenv()

@sync_to_async
def set_client(data):
    
    print(data)

    response = requests.get(data['img'], stream=True)    
    response.raise_for_status()

    with open(f'{data["user_id"]}.jpg', 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)
    

    m = VetClient()
    m.name = data['name']
    m.phone = data['phone']
    m.location = data['location']
    m.day = data['day']
    m.humidity = data['humidity']
    m.temperature = data['temperature']
    m.sickness = data['sickness']
    m.diagnose = data['diagnose']
    m.img = ImageFile(open(f"{data['user_id']}.jpg", "rb"))
    m.save()

    print(m)

    os.remove(f'{data["user_id"]}.jpg')

async def set_name_task(message: types.Message, state: FSMContext=None):


    user_id = message.from_user.id
    file_id = message.photo[-1].file_id  # get file_id of the photo

    await message.answer(texts.vet_finish)

    file_info = await bot.get_file(file_id)  # get file information

    img = "https://api.telegram.org/file/bot{}/{}".format(os.getenv('BOT_TOKEN'), file_info['file_path'])
   
    state_data = await state.get_data() 
    state_data['user_id'] = user_id
    state_data['img'] = img

    # await set_client(state_data)
    
    await bot.send_photo(
        chat_id=os.getenv("GROUP_CHAT_ID"),
        photo=file_id,
        caption=texts.vet_caption.format(
            state_data['name'],
            state_data['phone'],
            state_data['location'],
            state_data['day'],
            state_data['humidity'],
            state_data['temperature'],
            state_data['sickness'],
            state_data['diagnose'],
        )
    )
    await state.finish()
    
@dp.message_handler(content_types=['photo'], state=VetClientState.media)
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_name_task(message, state))
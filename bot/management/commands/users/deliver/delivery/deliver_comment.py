from django.core.files.images import ImageFile

import io
from aiogram import types
from aiogram.dispatcher import FSMContext
import requests

from ....loader import dp, bot
from .... import texts, buttons
from ....states import DeliveryState
from delivered.models import Delivered
import asyncio
from asgiref.sync import sync_to_async
from aiogram.types import InputMediaPhoto

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
    

    m = Delivered()
    m.name = data['name']
    m.phone = data['phone']
    m.location = data['location']
    m.day = data['price']
    m.img = ImageFile(open(f"{data['user_id']}.jpg", "rb"))
    m.save()

    os.remove(f'{data["user_id"]}.jpg')

async def set_name_task(message: types.Message, state: FSMContext=None):
    user_id = message.from_user.id
    file_id = message.photo[-1].file_id  # get file_id of the photo

    await message.answer(texts.finish_deliver)

    file_info = await bot.get_file(file_id)  # get file information

    img = "https://api.telegram.org/file/bot{}/{}".format(os.getenv('BOT_TOKEN'), file_info['file_path'])
   
    state_data = await state.get_data()
    state_data['user_id'] = user_id
    state_data['img'] = img

    await set_client(state_data)
    media_group = [
        InputMediaPhoto(media='', caption='Caption 1'),
        InputMediaPhoto(media='', caption='Caption 2'),
        # Add more media items as needed
    ]

    await bot.send_media_group(
        chat_id=os.getenv("GROUP_CHAT_ID"),
        media=media_group,
        caption=texts.deliver_caption.format(
            state_data['name'],
            state_data['phone'],
            state_data['location'],
            state_data['price'],
        )
    )
        

    await bot.send_media_group()(
        chat_id=os.getenv("GROUP_CHAT_ID"),
        photo=file_id,
        caption=texts.deliver_caption.format(
            state_data['name'],
            state_data['phone'],
            state_data['location'],
            state_data['price'],
        )
    )
    await state.finish()
    
@dp.message_handler(content_types=['photo'], state=DeliveryState.comment)
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_name_task(message, state))

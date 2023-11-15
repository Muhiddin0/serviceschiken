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

    d = Delivered()
    d.name = data['name']
    d.phone = data['phone']
    d.location = data['location']
    d.day = data['price']
    d.img = ImageFile(open(f"{data['user_id']}.jpg", "rb"))
    d.comment = data['comment']
    d.save()

    print(d)
    os.remove(f'{data["user_id"]}.jpg')


async def set_name_task(message: types.Message, state: FSMContext = None):
    chicken_img_file_id = message.photo[-1].file_id  # get file_id of the photo

    await message.answer(texts.deliver_comment)
    file_info = await bot.get_file(chicken_img_file_id)  # get file information

    state_data = await state.get_data()
    state_data['chicken_img_id'] = {
        "file_id":chicken_img_file_id,
        "file_path":file_info['file_path']
    } 

    await state.set_data(state_data)

    await DeliveryState.comment.set()


@dp.message_handler(content_types=['photo'], state=DeliveryState.media)
async def func(message: types.Message, state: FSMContext = None):
    asyncio.create_task(set_name_task(message, state))
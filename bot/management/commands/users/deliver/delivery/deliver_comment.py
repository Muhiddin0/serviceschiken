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

    chickens_img_file = "chichekn_".format(data['user_id'])
    comment_img_file = "chichekn_".format(data['user_id'])


    m = Delivered()
    m.name = data['name']
    m.phone = data['phone']
    m.location = data['location']
    m.price = data['price']
    m.img = ImageFile(open(f"{chickens_img_file}.jpg", "rb"))
    m.comment = data['comment']
    m.comment_img = ImageFile(open(f"{comment_img_file}.jpg", "rb"))

    os.remove(f'{data["user_id"]}.jpg')

async def set_name_task(message: types.Message, state: FSMContext=None):
    comment_img_file_id = message.photo[-1].file_id  # get file_id of the photo
    comment = message.caption  # get file_id of the photo

    await message.answer(texts.finish_deliver, reply_markup=buttons.start)

    file_info = await bot.get_file(comment_img_file_id)  # get file information
    state_data = await state.get_data()
    state_data['comment_img'] = {
        "file_id":comment_img_file_id,
        "file_path":file_info['file_path']
    } 

    state_data['comment'] = comment

    img = "https://api.telegram.org/file/bot{}/{}"
    
    bot_token = os.getenv('BOT_TOKEN')
    chat_id = os.getenv('GROUP_CHAT_ID')

    await sync_to_async(Delivered.objects.create)(
        name = state_data['name'],
        phone = state_data['phone'],
        location = state_data['location'],
        price = state_data['price'],
        img = img.format(bot_token, state_data['chicken_img_id']['file_path']),
        comment = state_data['comment'],
        comment_img = img.format(bot_token, state_data['comment_img']['file_path'])
    )
    caption=texts.deliver_caption.format(
        state_data['name'],
        state_data['phone'],
        state_data['location'],
        state_data['price'],
    )

    media_group = [
        InputMediaPhoto(media=state_data['chicken_img_id']['file_id'], caption=caption),
        InputMediaPhoto(media=state_data['comment_img']['file_id']),
    ]

    await set_client(state_data)
    await bot.send_media_group(
        chat_id=chat_id,
        media=media_group,
    )
        
    await state.finish()
    
@dp.message_handler(content_types=['photo'], state=DeliveryState.comment)
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_name_task(message, state))

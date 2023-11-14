from aiogram import types
from aiogram.dispatcher import FSMContext

from django.shortcuts import get_object_or_404

from delivered.models import DeliverUsers
from ...loader import dp, bot
from ... import texts, buttons
from ...states import DeliveryState
import asyncio

from asgiref.sync import sync_to_async



async def set_order_task(message: types.Message, state: FSMContext=None):
    user_id = message.from_user.id

    # user = await VetUsers.objects.async_filter(user_id=user_id)
    user = await sync_to_async(DeliverUsers.objects.filter)(user_id=user_id)

    print(user)

    if user is not None:

        if not len(user):
            await message.answer(texts.register_deliver, reply_markup=buttons.register)
            return

    await message.answer(texts.deliver_name)

    await DeliveryState.name.set()


@dp.message_handler(text='🚚 Yetkazib berish', content_types='text')
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_order_task(message, state))
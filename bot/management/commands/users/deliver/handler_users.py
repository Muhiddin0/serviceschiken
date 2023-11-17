from aiogram import types
from aiogram.dispatcher import FSMContext

from django.shortcuts import get_object_or_404

from delivered.models import DeliverUsers
from ...loader import dp, bot
from ... import texts, buttons
from ...states import DeliveryState, SupplierRegisterMenuState
import asyncio

from asgiref.sync import sync_to_async



async def set_order_task(message: types.Message, state: FSMContext=None):
    user_id = message.from_user.id

    user = await sync_to_async(DeliverUsers.objects.filter)(user_id=user_id)

    print(user)

    if not len(user):
        await message.answer(texts.register_deliver, reply_markup=buttons.register)
        await SupplierRegisterMenuState.menu.set()
        return

    if not user.first().status:
        await message.answer(texts.block_user)
        return

    await message.answer(texts.great, reply_markup=buttons.remove_keyboard)
    await message.answer(texts.deliver_name, reply_markup=buttons.cancel)

    await DeliveryState.name.set()


@dp.message_handler(text='🚚 Yetkazib berish', content_types='text')
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_order_task(message, state))
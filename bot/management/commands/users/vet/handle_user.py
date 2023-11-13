from aiogram import types
from aiogram.dispatcher import FSMContext

from django.shortcuts import get_object_or_404

from vet.models import VetUsers
from ...loader import dp, bot
from ... import texts, buttons
from ...states import VetRegister, VetClientState
import asyncio

from asgiref.sync import sync_to_async



async def set_order_task(message: types.Message, state: FSMContext=None):
    user_id = message.from_user.id

    # user = await VetUsers.objects.async_filter(user_id=user_id)
    user = await sync_to_async(VetUsers.objects.filter)(user_id=user_id)

    print(user)

    if user is not None:

        if not len(user):
            await message.answer(texts.register_vet, reply_markup=buttons.register)
            return

    await message.answer(texts.vet_client_name)

    await VetClientState.name.set()    


@dp.message_handler(text='🐣 Veterenariya', content_types='text')
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_order_task(message, state))
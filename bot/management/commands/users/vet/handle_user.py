from aiogram import types
from aiogram.dispatcher import FSMContext

from django.shortcuts import get_object_or_404

from vet.models import VetUsers
from ...loader import dp, bot
from ... import texts, buttons
from ...states import VetRegister, VetClientState, VetRegisterMenu
import asyncio

from asgiref.sync import sync_to_async



async def set_order_task(message: types.Message, state: FSMContext=None):
    user_id = message.from_user.id

    user = await sync_to_async(VetUsers.objects.filter)(user_id=user_id)

    if not len(user):
        await message.answer(texts.register_vet, reply_markup=buttons.register)
        await VetRegisterMenu.menu.set()
        return

    user = user.first()
    if not user.status:
        await message.answer(texts.block_user)
        return
    
    
    await message.answer(texts.great, reply_markup=buttons.remove_keyboard)
    await message.answer(texts.vet_client_name, reply_markup=buttons.cancel)

    await VetClientState.name.set()    


@dp.message_handler(text='🐣 Veterenariya', content_types='text')
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_order_task(message, state))
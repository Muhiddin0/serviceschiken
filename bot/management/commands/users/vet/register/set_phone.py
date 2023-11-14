from aiogram import types
from aiogram.dispatcher import FSMContext

from ....loader import dp, bot
from .... import texts, buttons
from ....states import VetRegister, VetClientState
from vet.models import VetUsers

import asyncio
from asgiref.sync import sync_to_async


async def set_phone_task(message: types.Message, state: FSMContext=None):
    user_id = message.from_user.id
    phone = message.contact.phone_number

    await message.answer(text=texts.finish_vet_register, reply_markup=buttons.start)
    
    data = await state.get_data()

    await sync_to_async(VetUsers.objects.create)(user_id=user_id, name=data['name'], phone=phone)
    
    await state.finish()
    
    
@dp.message_handler(content_types=types.ContentType.CONTACT, state=VetRegister.phone)
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_phone_task(message, state))
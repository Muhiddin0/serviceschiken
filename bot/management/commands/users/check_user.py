from aiogram import types
from aiogram.dispatcher import FSMContext

from ..loader import dp, bot
from .. import texts, buttons
from ..states import SupplierRegisterState, VetClientState
from delivered.models import DeliverUsers
from vet.models import VetUsers

import asyncio
from asgiref.sync import sync_to_async


async def check_deliver_task(callbac_data: types.CallbackQuery, state: FSMContext = None):

    text = callbac_data.message.text
    data_entites = callbac_data.message.entities
    print(data_entites)
    
    role_index_start= data_entites[0]['offset']
    role_index_end = data_entites[0]['length'] + role_index_start

    role = text[role_index_start:role_index_end]

    name_index_start = data_entites[1]['offset']
    name_index_end = data_entites[1]['length'] + name_index_start

    name = text[name_index_start:name_index_end]

    phone_index_start = data_entites[2]['offset']
    phone_index_end = data_entites[2]['length'] + phone_index_start

    phone = text[phone_index_start:phone_index_end]

    user_id = data_entites[3]['user']['id']

    if role == "Veterenar":
        await sync_to_async(VetUsers.objects.create)(
            user_id=user_id,
            name=name,
            phone=phone,
            status=True
        )
    else:
        await sync_to_async(DeliverUsers.objects.create)(
            user_id=user_id,
            name=name,
            phone=phone,
            status=True
        )

    await callbac_data.message.answer(text=texts.succes_register, reply_markup=buttons.start)

    await state.finish()


@dp.callback_query_handler(state='*', text_contains="set_delivered")
async def func(message: types.Message, state: FSMContext = None):
    asyncio.create_task(check_deliver_task(message, state))




# Unset
async def unset_deliver_task(callbac_data: types.CallbackQuery, state: FSMContext = None):
    data_entites = callbac_data.message.entities

    user_id = data_entites[2]['user']['id']

    await bot.send_message(
        chat_id=user_id,
            text=texts.fail
    )

@dp.callback_query_handler(state='*', text_contains="unset_deliver")
async def func(message: types.Message, state: FSMContext = None):
    
    asyncio.create_task(unset_deliver_task(message, state))

        
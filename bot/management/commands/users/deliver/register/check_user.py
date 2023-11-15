from aiogram import types
from aiogram.dispatcher import FSMContext

from ....loader import dp, bot
from .... import texts, buttons
from ....states import SupplierRegisterState, VetClientState
from delivered.models import DeliverUsers

import asyncio
from asgiref.sync import sync_to_async


async def check_deliver_task(callbac_data: types.CallbackQuery, state: FSMContext = None):
    text = callbac_data.message.text
    data_entites = callbac_data.message.entities
    
    name_index_start = data_entites[0]['offset']
    name_index_end = data_entites[0]['length'] + name_index_start

    phone_index_start = data_entites[1]['offset']
    phone_index_end = data_entites[1]['length'] + phone_index_start

    user_id = data_entites[2]['user']['id']

    await sync_to_async(DeliverUsers.objects.create)(
        user_id=user_id,
        name=text[name_index_start] + text[name_index_end],
        phone=text[phone_index_start] + text[phone_index_end],
        status=True
    )

    await callbac_data.message.answer(text=texts.succes_register, reply_markup=buttons.start)


    await state.finish()


@dp.callback_query_handler(state='*', text_contains="set_delivered")
async def func(message: types.Message, state: FSMContext = None):
    asyncio.create_task(check_deliver_task(message, state))




# Unset
async def unset_deliver_task(callbac_data: types.CallbackQuery, state: FSMContext = None):
    user_id = callbac_data.message.from_user.id
    phone = callbac_data.message.contact.phone_number
    await callbac_data.message.answer(text=texts.finish_del_register, reply_markup=buttons.start)

    data = await state.get_data()

    await state.finish()

@dp.callback_query_handler(state='*', text_contains="unset_deliver")
async def func(message: types.Message, state: FSMContext = None):
    
    asyncio.create_task(unset_deliver_task(message, state))

        
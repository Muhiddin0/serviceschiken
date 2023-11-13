from aiogram.dispatcher.filters.state import StatesGroup, State

class SupplierRegisterState(StatesGroup):
    name = State()
    phone = State()


class DeliveryState(StatesGroup):
    name = State()
    phone = State()
    location = State()
    count = State()
    image = State()
    comment = State()

    
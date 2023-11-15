from aiogram.dispatcher.filters.state import StatesGroup, State

class VetRegisterMenu(StatesGroup):
    menu = State()

class VetRegister(StatesGroup):
    name = State()
    phone = State()

class VetClientState(StatesGroup):
    name = State()
    phone = State()
    location = State()
    day = State()
    humidity = State()
    temperature = State()
    sickness = State()
    diagnose = State()
    media = State()

    
class OrderState(StatesGroup):
    name = State()
    phone = State()
    day = State()
    price = State()
    location = State()


class SupplierRegisterMenuState(StatesGroup):
    menu = State()

class SupplierRegisterState(StatesGroup):
    name = State()
    phone = State()


class DeliveryState(StatesGroup):
    name = State()
    phone = State()
    location = State()
    price = State()
    count = State()
    media = State()
    comment = State()
    

    
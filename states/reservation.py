from aiogram.fsm.state import State, StatesGroup

class ReserStateGroup(StatesGroup):
    number_product = State()
    delivery_method = State()
    full_name = State()
    address = State()
    phone_numb = State()

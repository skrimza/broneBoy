from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


first_panel_rkb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder='Выберите действие',
    keyboard=[
        [
            KeyboardButton(text='Чем занимается LIBERTINA❔')
        ],
        [
            KeyboardButton(text='Хочу посмотреть работы LIBERTINA❕')
        ]
    ]
)


second_panel_rkb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder='Выберите действие',
    keyboard=[
        [
            KeyboardButton(text='Хочу посмотреть работы LIBERTINA❕')
        ]
    ]
)

delivery_method_rkb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder='Выберите способ доставки',
    keyboard=[
        [
            KeyboardButton(text='Европочта'),
            KeyboardButton(text='Белпочта')
        ],
        [
            KeyboardButton(text='Самовывоз'),
            KeyboardButton(text='Доставка')
        ]
    ]
)

conditions_rkb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    input_field_placeholder='Выберите действие',
    keyboard=[
        [
            KeyboardButton(text='ДА!'),
            KeyboardButton(text='Нет!')
        ]
    ]
)


admin_button = KeyboardButton(text='Администратор')
finished_button = KeyboardButton(text='Закончить работу')
cancel_button = KeyboardButton(text='Отмена действий')
phone_button = KeyboardButton(text="Поделиться ☎️", request_contact=True)
first_panel_rkb.keyboard.append([admin_button, finished_button])
second_panel_rkb.keyboard.append([admin_button, finished_button])
delivery_method_rkb.keyboard.append([admin_button, finished_button])

action_builder = ReplyKeyboardBuilder()
action_builder.add(admin_button, finished_button)
method_builder = ReplyKeyboardBuilder()
method_builder.add(admin_button, finished_button, cancel_button)
method_builder.adjust(1)
phone_builder = ReplyKeyboardBuilder()
phone_builder.add(phone_button, admin_button, cancel_button, finished_button)
phone_builder.adjust(2)

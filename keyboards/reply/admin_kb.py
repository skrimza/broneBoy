from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

basic_menu_rkb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder='Выбери раздел',
    keyboard=[
        [
            KeyboardButton(text='Добавить позицию')
        ],
        [
            KeyboardButton(text='удалить позицию')
        ],
        [
            KeyboardButton(text='Все позиции')
        ]
    ]
)


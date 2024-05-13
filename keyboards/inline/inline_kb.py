from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

choise_category_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Футболки', 
                                 callback_data='t-shirt'),
        ],
        [
            InlineKeyboardButton(text='Свитшоты', 
                                 callback_data='sweatshirt')
        ]
    ]
)

choise_question_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Да😍',
                                 callback_data='yes')
            # сюда кнопку нет
        ],
        [
            InlineKeyboardButton(text='А можно заказать?🥰',
                                 callback_data='order')
        ]
    ]
)

control_choise_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='ДА!',
                                 callback_data='sure'),
            # сюда кнопку нет
        ]
    ]
)


negative_button = InlineKeyboardButton(text='Нет😢', callback_data='no')
choise_question_ikb.inline_keyboard[0].append(negative_button)
control_choise_ikb.inline_keyboard[0].append(negative_button)

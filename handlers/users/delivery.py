from aiogram import F, Router
from aiogram.types import Message, BufferedInputFile
from settings import BASE_DIR
from aiogram.fsm.context import FSMContext
from states import ReserStateGroup
from utils.models import UserReservation
from .handlers import router
from keyboards.reply.main_kb import (
    delivery_method_rkb,
    conditions_rkb,
    method_builder,
    phone_builder
)

router = Router()

@router.message(ReserStateGroup.number_product)
async def get_num_product(message: Message, state: FSMContext):
    try:
        num_product = int(message.text)
    except ValueError:
        await message.answer(
            text='Неверный номер изделия!'
        )
    else:
        if num_product < 8: # надо изменить по количеству в базе данных
            await state.clear()
            await message.answer(text=f'Номер изделия: {message.text}')
            await state.update_data({'number_product': num_product})
            await state.set_state(ReserStateGroup.delivery_method)
            await message.answer_photo(photo=BufferedInputFile.from_file(
                                            path=BASE_DIR / 'static/delivery.png'
                                        ), 
                                       caption='<b>Выберите способ доставки!</b>', 
                                       reply_markup=delivery_method_rkb)
        else:
            await message.answer(
                text='Неверный номер изделия!'
            )


@router.message(ReserStateGroup.delivery_method)
async def get_delivery_method(message: Message, state: FSMContext):
    deliv = message.text
    await message.delete()
    await message.answer(text=f'Способ доставки: {message.text}')
    await state.clear()
    await state.update_data({'delivery_method': deliv})
    if deliv == 'Самовывоз':
        await message.answer(text='На данный момент, вы можете забрать'\
                                    ' свое изделие по адресу: г.Минск,'\
                                    ' проспект Победителей 5, магазин'\
                                    ' кроссовок "СНИКЕРХЭД". Ваше'\
                                    ' изделие будет там уже завтра,'\
                                    ' Вы готовы подтвердить Ваш заказ?',
                                    reply_markup=conditions_rkb)
    elif deliv == 'Европочта':
        await state.set_state(ReserStateGroup.full_name)
        await message.answer(text='<b>Введите Фамилию, Имя, Отчество</b> через пробел.'\
                                'Например: Петрова Анна Николаевна', reply_markup=method_builder.as_markup(resize_keyboard=True))
    elif deliv == 'Белпочта':
        await state.set_state(ReserStateGroup.full_name)
        await message.answer(text='<b>Введите Фамилию, Имя, Отчество</b> через пробел.'\
                                'Например: Петрова Анна Николаевна', reply_markup=method_builder.as_markup(resize_keyboard=True))
    elif message.text == 'Доставка':
        await state.set_state(ReserStateGroup.full_name)
        await message.answer(text='Введите фамилию и имя получателя!',
                             reply_markup=method_builder.as_markup(resize_keyboard=True))
        
# ответ да по самовывозу
@router.message(F.text == conditions_rkb.keyboard[0][0])
async def pos_pickup(message: Message):
    await message.delete()
    await message.answer(text='Cупер! Оставьте, пожалуйста, свой мобильный телефон, и Наш менеджер Вам перезвонит!')
    # и тут мне пришла в голову идея!!!! надо записать!!! и подумать


@router.message(ReserStateGroup.full_name)
async def get_fullname(message: Message, state: FSMContext):
    f_name = message.text
    await message.answer(text=f_name)
    await state.clear()
    await state.update_data({'full_name': f_name})
    await state.set_state(ReserStateGroup.address)
    await message.answer(text='Введите адрес доставки с указанием Вашего индекса,'\
                                '(Если Европочта, то укажите номер отделения)'\
                                'Например: [индекс/отделение], [Город], [улица], [дом-квартира]:')
        
#  ввод адреса доставки
@router.message(ReserStateGroup.address)
async def get_address(message: Message, state: FSMContext):
    address = message.text
    await message.answer(text=f'Адрес доставки: {message.text}')
    await state.clear()
    await state.update_data({'address': address})
    await state.set_state(ReserStateGroup.phone_numb)
    await message.answer('Мы уже на финишной прямой! Последнее,'\
                            ' что мне необходимо, это Ваш мобильный'\
                            ' телефон для связи с Вами, а так же,'\
                            ' чтобы Вы могли получить оповещение о'\
                            ' прибытии заказа на пункт выдачи!',
                            reply_markup=phone_builder.as_markup(resize_keyboard=True))


@router.message(ReserStateGroup.phone_numb)
async def thanks_giving(message: Message):
    phone_num = message.contact
    await message.answer(text=f'номер телефона: {phone_num.phone_number}')
    async with UserReservation.session() as resersession:
        await message.answer('')
    

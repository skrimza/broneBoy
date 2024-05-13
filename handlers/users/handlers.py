from aiogram import F, Router
from aiogram.types import Message, CallbackQuery, BufferedInputFile
from aiogram.fsm.context import FSMContext
from utils.models import User
# from .router import router
from sqlalchemy.exc import IntegrityError
from settings import BASE_DIR
from states import ReserStateGroup
from keyboards.reply.main_kb import (
    first_panel_rkb,
    second_panel_rkb,
    action_builder,
    
)
from keyboards.reply.admin_kb import (
    basic_menu_rkb
)
from keyboards.inline import (choise_category_ikb,
                                choise_question_ikb,
                                control_choise_ikb)

router = Router()

@router.message(F.text.startswith('/start'))
async def start_command(message: Message):
    user = User(id=message.from_user.id)
    text = ''
    markup = None
    async with User.session() as session:
        # await session.execute(User.__table__.delete())
        # await session.commit()
        session.add(user)
        try:
            await session.commit()
        except IntegrityError:
            if user.id == 874255780:
                text = 'Привет, Александра, давай поработаем!'
                markup = basic_menu_rkb
            else:
                text = f'Добрый день, {message.from_user.first_name}, чем я могу быть полезен сегодня для тебя?'
                markup = second_panel_rkb
        else:
            text = f'Добрый день, {message.from_user.first_name}! я бот, помощник нашей дорогой Libertina! Могу ли быть для тебя полезным?)'
            markup = first_panel_rkb
        finally:
            await message.answer(text=text, reply_markup=markup)

# Знакомство с Libertina
@router.message(F.text == first_panel_rkb.keyboard[0][0].text)
async def info_handler(message: Message):
    await message.answer_photo(
        photo=BufferedInputFile.from_file(
            path=BASE_DIR / 'static/image1.jpg'
        ),
        caption='Libertina - это искусство на одежде,' \
                    ' которое подчеркивает индивидуальность и изысканность.' \
                    ' Создатель данного проекта, Александра, воплощает женственность' \
                    ' и красоту, рисуя уникальные образы девушек на футболках и' \
                    ' свитшотах в единственном экземпляре для Вас.', 
                    reply_markup=second_panel_rkb
    )
 
# Выбор категории изделий
@router.message(F.text == first_panel_rkb.keyboard[1][0].text or F.text == second_panel_rkb.keyboard[0][0].text)
async def choise(message: Message):
    await message.delete()
    await message.answer(text='Хорошо, я покажу работы Александры,'\
                        ' но для начала необходимо выбрать категорию изделий!', 
                        reply_markup=choise_category_ikb)


# здесь должен сработать выбор базы данных и предложен просмотр изделий пользователю
@router.callback_query(F.data == 't-shirt')
async def choise_tshirt(callback: CallbackQuery):
    category = 'майки'
    await callback.message.answer(text='Что-нибудь понравилось?',
                                    reply_markup=choise_question_ikb)


@router.callback_query(F.data == 'sweatshirt')
async def choise_sweatshirt(callback: CallbackQuery):
    category = 'свитшоты'
    await callback.message.answer(text='Что-нибудь понравилось?',
                                    reply_markup=choise_question_ikb)

# если ответ от пользователя да
@router.callback_query(F.data == 'yes')
async def agreement(callback: CallbackQuery):
    await callback.message.answer(text='Отлично!👌 не желаешь ли оформить заказ?)'\
                                        ' Я много времени не займу, буквально пару минут'\
                                        ' и всё! Так же можно связаться с Администратором'\
                                        ' для выполнения изделия на заказ, и отменить'\
                                        ' последние действия, если нужно повременить с заказом!',
                                    reply_markup=control_choise_ikb)

# здесь пошло оформление заказа для клиента
@router.callback_query(F.data == 'sure')
async def place_order(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='Отлично!👌 Тогда приступим!'\
                                        ' Для начала напиши мне номер'\
                                        ' изделия, которое понравилось!'\
                                        ' оно написано под фотографией изделия!')
    await state.set_state(ReserStateGroup.number_product)
    await callback.message.answer(text='<b>Введите номер изделия!</b>')


    
# если пользователь ответил нет
@router.callback_query(F.data == 'no')
async def refusal(callback: CallbackQuery):
    await callback.message.answer(text='Мне очень жаль, что Вы не смогли найти то, что Вам по душе😔'\
                                        ' Может я могу Вас соединить с администратором, чтобы Вы'\
                                        ' могли оформить на заказ изделие, или все же вы желаете закончить работу?',
                                        reply_markup=action_builder.as_markup(resize_keyboard=True))


# @router.message(F.text == first_panel_rkb.keyboard[2][1].text or F.text == second_panel_rkb.keyboard[1][1].text)
# async def creative_work(message: Message):
#     await message.answer(text=f'Спасибо, {message.from_user.first_name}, за то,'\
#                                ' что воспользовались ботом. будем с радостью'\
#                                 ' ждать Вас снова!🌿 Хорошего Вам дня!)')

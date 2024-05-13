from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from settings import BASE_DIR
from aiogram.fsm.context import FSMContext
from keyboards.reply.admin_kb import (
    basic_menu_rkb
)

router = Router()

@router.message(F.text == basic_menu_rkb.keyboard[0][0].text)
async def  add_position(message: Message):
    pass


@router.message(F.text == basic_menu_rkb.keyboard[1][0].text)
async def delete_position(message: Message):
    pass


@router.message(F.text == basic_menu_rkb.keyboard[2][0].text)
async def view_position (message: Message):
    pass

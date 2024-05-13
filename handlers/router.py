from aiogram import Router

from .users import (handlers,
                    delivery)

router = Router()
router.include_routers(handlers.router,
                       delivery.router)
from aiogram import Router
from .start import router as start_router
from .order import router as orders_router
from Support.order import router as support_router
from GetNumber.order import router as get_number_router

router = Router()

router.include_router(start_router)
router.include_router(orders_router)
router.include_router(support_router)
router.include_router(get_number_router)
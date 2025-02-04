from router.strategy_exec_info import fastapi_app
from tortoise.contrib.fastapi import register_tortoise
from config import settings

register_tortoise(
    fastapi_app,
    db_url=settings.db.url,
    modules={"models": ["models"]},
    generate_schemas=False,
    add_exception_handlers=True
)
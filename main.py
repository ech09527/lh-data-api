from router.strategy_exec_info import fastapi_app
from tortoise.contrib.fastapi import register_tortoise

register_tortoise(
    fastapi_app,
    db_url="mysql://lh3_api:ECF7773F15@rm-j6c4gtw0039u0ia32ko.mysql.rds.aliyuncs.com:3306/lh3_test",
    modules={"models": ["models"]},
    generate_schemas=False,
    add_exception_handlers=True
)
from tortoise import Tortoise
import tortoise
from models import StrategyExecInfo
import pytest
from config import settings

@pytest.fixture(autouse=True)
async def init_tortoise():
    await Tortoise.init(
        db_url=settings.db.url,
        modules={'models': ['models']}
    )
    await Tortoise.generate_schemas()

@pytest.mark.asyncio
async def test_q():
    # await StrategyExecInfo.all().filter(completed='Y').get_or_none()
    conn = Tortoise.get_connection('default')
    r = await conn.execute_query('select * from strategy_exec_info where id = "Y"')
    pass


@pytest.mark.asyncio
async def test_q1():
    from services import paging_service
    paging_service.set_page_param(1,20)
    res = await paging_service.tortoise_paging(StrategyExecInfo.all())
    for item in res.items:
        print(item.id)
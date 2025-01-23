from tortoise import Tortoise
from models import StrategyExecInfo
import pytest

@pytest.fixture(autouse=True)
async def init_tortoise():
    await Tortoise.init(
        db_url="mysql://lh3:6EBD014A76@rm-j6c4gtw0039u0ia32ko.mysql.rds.aliyuncs.com:3306/lh3_test",
        modules={'models': ['models']}
    )
    await Tortoise.generate_schemas()

@pytest.mark.asyncio
async def test_q():
    await StrategyExecInfo.all().filter(id=1).get_or_none()
    pass
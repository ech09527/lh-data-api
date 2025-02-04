from fastapiapp import fastapi_app
from datetime import datetime
from models import StrategyExecInfo
from services import paging_service
from common.fastapi_tortoise_page import paging
from tortoise.contrib.pydantic import pydantic_model_creator
from common.respbody import common_resp

@fastapi_app.get("/strategy_exec_info")
@common_resp
@paging
async def list_strategy_exec_info(
    start_time: datetime = None, 
    end_time: datetime = None,
    completed: str = None) -> StrategyExecInfo:
    
    query = StrategyExecInfo.all()
    if start_time:
        query = query.filter(start_time__gte=start_time)
    if end_time:
        query = query.filter(start_time__lte=end_time)
    if completed:
        query = query.filter(completed=completed)
    return query

@fastapi_app.get("/strategy_exec_info2")
async def test():
    res = await StrategyExecInfo.all().first()
    m = pydantic_model_creator(StrategyExecInfo)
    res = m.from_orm(res)
    return res
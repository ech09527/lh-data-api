from pydantic import BaseModel
from typing import List,TypeVar,Generic
from loguru import logger
from functools import wraps

RESP_BODY_DATA_TYPE = TypeVar('T')
class RespBody(BaseModel, Generic[RESP_BODY_DATA_TYPE]):
    status: int = 0
    msg: str = None
    data: RESP_BODY_DATA_TYPE = None
    
    

def common_resp(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            res = await func(*args, **kwargs)
        except Exception as e:
            logger.error(e)            
            return RespBody(status=1,msg=str(e))
        return RespBody(data=res)
    wrapper.__annotations__['return'] = RespBody[func.__annotations__['return']]
    return wrapper
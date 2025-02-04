from pydantic import BaseModel
from typing import List,TypeVar,Generic, Union
from loguru import logger
from functools import wraps
from traceback import format_exc
RESP_BODY_DATA_TYPE = TypeVar('T')
class RespBody(BaseModel, Generic[RESP_BODY_DATA_TYPE]):
    status: int = 0
    msg: Union[str, None]
    data: Union[RESP_BODY_DATA_TYPE, None]
    
    

def common_resp(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            res = await func(*args, **kwargs)
            res = RespBody(data=res,msg="success",status=0)
        except Exception as e:
            logger.error(format_exc())
            res = RespBody(status=1,msg=str(e),data=None)
        return res
    wrapper.__annotations__['return'] = RespBody[func.__annotations__['return']]
    return wrapper
import contextvars
from typing import List,TypeVar,Generic
from tortoise.queryset import QuerySet
from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import BaseModel
import math
from functools import wraps

PAGE_PARAM  = contextvars.ContextVar("tortoise_orm_page_param")
PAGE_RESULT_ITEM_TYPE = TypeVar('T')

class PageResult(BaseModel, Generic[PAGE_RESULT_ITEM_TYPE]):
    size: int
    page: int
    total: int
    pages: int
    items: List[PAGE_RESULT_ITEM_TYPE]
    
def set_page_param(page:int = 1, page_size:int = 20):
    PAGE_PARAM.set(
        {
            "page": page,
            "size": page_size
        }
    )

async def tortoise_paging(query_set:QuerySet):
    param = PAGE_PARAM.get(None)
    if  param is None:
        page = 1
        size = 20
    else:
        page = param['page']
        size = param['size']
    offset = (page - 1) * size
    res =  await query_set.limit(size).offset(offset)
    count = await query_set.count()
    pages =  math.ceil(count / size)
    data = {
        "size": size,
        "page": page,
        "items": res,
        "total": count,
        "pages": pages
    }
    ret = PageResult(**data)
    return ret

def paging(func) -> PageResult:
    @wraps(func)
    async def wrapper(*args, **kwargs):
        res = await func(*args, **kwargs)
        return await tortoise_paging(res)
    t = pydantic_model_creator(func.__annotations__['return'])
    wrapper.__annotations__['return'] = PageResult[t]
    return wrapper

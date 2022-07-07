# conding:utf-8


from typing import Optional

from fastapi import APIRouter, Header, Request, Body

# main的分路由
from utils.picUtil import savePic

main_app = APIRouter()


@main_app.post("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None, accesstoken: str = Header(None), req: Request = None):
    """
    测试调用服务
    :param item_id:
    :param q:
    :param accesstoken:
    :param req:
    :return:
    """
    return {"item_id": item_id, "q": q, "test": accesstoken, "header": req.headers}


@main_app.post("/Subscribe/Verify")
async def test(req: Request = None, body=Body(...)):
    print("订阅消息内容")
    print(body)
    savePic(body)
    rescode = {"code": 200, "desc": 'ok'}
    return rescode


@main_app.post("/Subscribe/Snap")
async def test(body=Body(...), req: Request = None):
    print("陌生人消息")
    print(body)
    rescode = {"code": 200, "desc": 'ok'}
    return rescode


@main_app.post("/Subscribe/heartbeat")
async def test(req: Request = None):
    print("心跳响应")
    rescode = {"code": 200, "desc": 'ok'}
    return rescode


@main_app.post("/Subscribe/IDCard")
async def test(body=Body(...), req: Request = None):
    print("身份证消息")
    print(body)
    rescode = {"code": 200, "desc": 'ok'}
    return rescode



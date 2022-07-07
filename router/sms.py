# coding:utf-8
import time
from random import uniform

from fastapi import APIRouter, Response, Cookie

from client.CommonClient import Client

# sms的分路由
sms_app = APIRouter()


@sms_app.post("/code")
async def send_sms(mobile: str, code: str = None, flag: float = Cookie(0), response: Response = None):
    """
    发送短信验证码的功能，因为短信服务提供商的原因，现在只能用验证码
    :param mobile:
    :param code:
    :return:
    """
    if flag + 60 * 2 > time.time():
        return {"error": "发送时间间隔过短"}
    if code is None:
        tem = int(uniform(1, 10) * 100000)
        code = str(tem)
        print(code)
    content = '【中电三公司】你的验证码是：{}，5分钟内有效！'.format(code)
    result = Client.send_sms(mobile, content)
    # result = "测试数据"
    result = {"code": code, "result": result}
    response.set_cookie("flag", time.time())
    return result

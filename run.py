import time

import uvicorn
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

import nacos_app
from config import myConfig
from router.main import main_app
from router.orc import ocr_app
from router.sms import sms_app

app = FastAPI(
    title='快速调用接口',
    description='验证项目，先验证一下接口是否可用，后续再重构java',
    version='1.0.0',
    docs_url='/docs',
    redoc_url='/redocs',
)


# 拦截器的例子
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://192.168.0.18:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main_app, prefix="", tags=["mainController"])

if __name__ == '__main__':
    # nacos_app.start()
    uvicorn.run(app='run:app', host="0.0.0.0", port=myConfig.port, reload=True, debug=True, log_level="warning")

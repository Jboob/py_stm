#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 17:38
# @Author  : 微信公众号 ProgrammerRan 作者
# @Site    : 
# @File    : main.py
# @Software: PyCharm
import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router

from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# 跨域设置
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# 路由配置
app.include_router(api_router, prefix=settings.API_V1_STR)

# 启动入口
if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1", port=8088, reload=True, debug=True)

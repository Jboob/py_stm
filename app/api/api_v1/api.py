#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 17:49
# @Author  : 微信公众号 ProgrammerRan 作者
# @Site    : 
# @File    : api.py
# @Software: PyCharm

from fastapi import APIRouter

from app.api.api_v1 import login, users, courses

api_router = APIRouter()
api_router.include_router(login.router, tags=["用户登录"])
api_router.include_router(users.router, prefix="/users", tags=["用户信息"])
api_router.include_router(courses.router, tags=["课程"])


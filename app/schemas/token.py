#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/19 17:21
# @Author  : 微信公众号 ProgrammerRan 作者
# @Site    : 
# @File    : token.py
# @Software: PyCharm
from typing import Optional

from pydantic import BaseModel


# Token Response
class Token(BaseModel):
    access_token: str
    token_type: str


# 定义写入内容
class TokenPayload(BaseModel):
    sub: Optional[str] = None

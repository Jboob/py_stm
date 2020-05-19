#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 17:42
# @Author  : 微信公众号 ProgrammerRan 作者
# @Site    : 
# @File    : config.py
# @Software: PyCharm
import secrets
from typing import List, Optional, Union, Dict, Any

from pydantic import BaseSettings, AnyHttpUrl, HttpUrl, validator
from sqlalchemy.dialects.mysql import pymysql


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str = 'http://127.0.0.1'
    SERVER_HOST: str = '127.0.0.1'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ['http://127.0.0.1']

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str = '学生管理系统 API'
    SENTRY_DSN: Optional[HttpUrl] = None

    MYSQL_SERVER: str = ''
    MYSQL_USER: str = 'root'
    MYSQL_PASSWORD: str = '123456'
    MYSQL_DB: str = 'stm'
    SQLALCHEMY_DATABASE_URI: str = 'mysql+pymysql://root:123456@localhost:3306/stm?charset=utf8'


class Config:
    case_sensitive = True


settings = Settings()

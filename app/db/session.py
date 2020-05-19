#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 11:27
# @Author  : 微信公众号 ProgrammerRan 作者
# @Site    : 
# @File    : session.py
# @Software: PyCharm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

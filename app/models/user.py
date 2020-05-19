#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 10:28
# @Author  : 微信公众号 ProgrammerRan 作者
# @Site    : 
# @File    : userInfo.py
# @Software: PyCharm
from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String

from ..db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


class User(Base):
    __tablename__ = "tb_user"
    id = Column(Integer, primary_key=True, index=True)
    userName = Column(String, index=True)
    userPass = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    mobile = Column(String, unique=True, nullable=False)
    regTime = Column(String, nullable=False)
    loginTime = Column(String, nullable=True)
    is_active = Column(Integer, default=1)

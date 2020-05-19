#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 11:26
# @Author  : 微信公众号 ProgrammerRan 作者
# @Site    : 
# @File    : base_class.py
# @Software: PyCharm
from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    id: Any
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

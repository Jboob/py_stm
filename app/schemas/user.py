#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 11:41
# @Author  : 微信公众号 ProgrammerRan 作者
# @Site    : 
# @File    : user.py
# @Software: PyCharm

from typing import Optional

from pydantic import BaseModel, EmailStr


# 公共字段
class UserBase(BaseModel):
    userName: Optional[str] = None
    email: Optional[EmailStr] = None
    mobile: Optional[str]
    is_active: Optional[int] = True


# 创建用户字段
class UserCreate(UserBase):
    userPass: str


# 更新用户
class UserUpdate(UserBase):
    userPass: str


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class User(UserInDBBase):
    pass


class UserInDB(UserInDBBase):
    userPass: str
